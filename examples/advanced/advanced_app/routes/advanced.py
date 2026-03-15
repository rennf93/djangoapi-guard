from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from advanced_app.models import message_response
from advanced_app.security import guard


@require_GET
@guard.time_window(start_time="09:00", end_time="17:00", timezone="UTC")
def business_hours_only(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Access granted during business hours",
            details={"hours": "09:00-17:00 UTC"},
        )
    )


@require_GET
@guard.time_window(start_time="00:00", end_time="23:59", timezone="UTC")
def weekend_endpoint(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Weekend access endpoint",
            details={
                "note": "Implement weekend check in time_window",
            },
        )
    )


@csrf_exempt
@require_POST
@guard.honeypot_detection(["honeypot_field", "trap_input", "hidden_field"])
def honeypot_detection(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Human user verified",
            details={"honeypot_status": "clean"},
        )
    )


@require_GET
@guard.suspicious_detection(enabled=True)
def detect_suspicious_patterns(request: HttpRequest) -> JsonResponse:
    query = request.GET.get("query")
    return JsonResponse(
        message_response(
            "No suspicious patterns detected",
            details={"query": query},
        )
    )


urlpatterns = [
    path("business-hours", business_hours_only),
    path("weekend-only", weekend_endpoint),
    path("honeypot", honeypot_detection),
    path("suspicious-patterns", detect_suspicious_patterns),
]
