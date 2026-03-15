from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_GET

from advanced_app.models import auth_response, message_response
from advanced_app.security import guard


@require_GET
@guard.require_https()
def https_required_endpoint(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "HTTPS connection verified",
            details={"protocol": request.scheme},
        )
    )


@require_GET
@guard.require_auth(type="bearer")
def bearer_authentication(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        auth_response(
            authenticated=True,
            user="example_user",
            method="bearer",
            permissions=["read", "write"],
        )
    )


@require_GET
@guard.api_key_auth(header_name="X-API-Key")
def api_key_authentication(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        auth_response(
            authenticated=True,
            user="api_user",
            method="api_key",
            permissions=["read"],
        )
    )


@require_GET
@guard.require_headers(
    {
        "X-Custom-Header": "required-value",
        "X-Client-ID": "required-value",
    }
)
def require_custom_headers(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Required headers verified",
            details={"headers": dict(request.headers)},
        )
    )


urlpatterns = [
    path("https-only", https_required_endpoint),
    path("bearer-auth", bearer_authentication),
    path("api-key", api_key_authentication),
    path("custom-headers", require_custom_headers),
]
