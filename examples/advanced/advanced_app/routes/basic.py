import json
from ipaddress import ip_address
from typing import Any

from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from advanced_app.models import health_response, ip_info_response, message_response


@require_GET
def basic_root(request: HttpRequest) -> JsonResponse:
    return JsonResponse(message_response("Basic features endpoint"))


@require_GET
def get_ip_info(request: HttpRequest) -> JsonResponse:
    client_ip = "unknown"
    remote_addr = request.META.get("REMOTE_ADDR", "")
    if remote_addr:
        try:
            client_ip = str(ip_address(remote_addr))
        except ValueError:
            client_ip = remote_addr

    return JsonResponse(
        ip_info_response(
            ip=client_ip,
            country="US",
            city="Example City",
            region="Example Region",
            is_vpn=False,
            is_cloud=False,
        )
    )


@require_GET
def health_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse(health_response("healthy"))


@csrf_exempt
@require_POST
def echo_request(request: HttpRequest) -> JsonResponse:
    data: dict[str, Any] = {}
    if request.body:
        try:
            data = json.loads(request.body)
        except (json.JSONDecodeError, ValueError):
            data = {}
    return JsonResponse(
        message_response(
            "Echo response",
            details={
                "data": data,
                "headers": dict(request.headers),
                "method": request.method,
                "url": request.build_absolute_uri(),
            },
        )
    )


urlpatterns = [
    path("", basic_root),
    path("ip", get_ip_info),
    path("health", health_check),
    path("echo", echo_request),
]
