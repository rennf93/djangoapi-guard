import json
from typing import Any

from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from advanced_app.models import message_response


@csrf_exempt
@require_POST
def test_xss_detection(request: HttpRequest) -> JsonResponse:
    raw: Any = {}
    if request.body:
        try:
            raw = json.loads(request.body)
        except (json.JSONDecodeError, ValueError):
            raw = {}
    payload = raw if isinstance(raw, str) else raw.get("payload", "")
    return JsonResponse(
        message_response(
            "XSS test payload processed",
            details={"payload": payload, "detected": False},
        )
    )


@require_GET
def test_sql_injection(request: HttpRequest) -> JsonResponse:
    query = request.GET.get("query", "")
    return JsonResponse(
        message_response(
            "SQL injection test processed",
            details={"query": query, "detected": False},
        )
    )


@require_GET
def test_path_traversal(request: HttpRequest, file_path: str) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Path traversal test",
            details={"path": file_path, "detected": False},
        )
    )


@csrf_exempt
@require_POST
def test_command_injection(request: HttpRequest) -> JsonResponse:
    raw: Any = {}
    if request.body:
        try:
            raw = json.loads(request.body)
        except (json.JSONDecodeError, ValueError):
            raw = {}
    command = raw if isinstance(raw, str) else raw.get("command", "")
    return JsonResponse(
        message_response(
            "Command injection test processed",
            details={"command": command, "detected": False},
        )
    )


@csrf_exempt
@require_POST
def test_mixed_attack(request: HttpRequest) -> JsonResponse:
    data = {}
    if request.body:
        try:
            data = json.loads(request.body)
        except (json.JSONDecodeError, ValueError):
            data = {}
    return JsonResponse(
        message_response(
            "Mixed attack test processed",
            details={
                "xss_test": data.get("input"),
                "sql_test": data.get("query"),
                "path_test": data.get("path"),
                "cmd_test": data.get("cmd"),
                "honeypot": data.get("honeypot_field"),
            },
        )
    )


urlpatterns = [
    path("xss-test", test_xss_detection),
    path("sql-injection", test_sql_injection),
    path("path-traversal/<path:file_path>", test_path_traversal),
    path("command-injection", test_command_injection),
    path("mixed-attack", test_mixed_attack),
]
