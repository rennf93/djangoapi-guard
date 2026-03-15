from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_GET

from advanced_app.models import message_response
from advanced_app.security import guard


@require_GET
@guard.rate_limit(requests=5, window=60)
def custom_rate_limit(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Custom rate limit endpoint",
            details={"limit": "5 requests per 60 seconds"},
        )
    )


@require_GET
@guard.rate_limit(requests=1, window=10)
def strict_rate_limit(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Strict rate limit endpoint",
            details={"limit": "1 request per 10 seconds"},
        )
    )


@require_GET
@guard.geo_rate_limit(
    {
        "US": (100, 60),
        "CN": (10, 60),
        "RU": (20, 60),
        "*": (50, 60),
    }
)
def geographic_rate_limiting(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        message_response(
            "Geographic rate limiting applied",
            details={"description": "Rate limits vary by country"},
        )
    )


urlpatterns = [
    path("custom-limit", custom_rate_limit),
    path("strict-limit", strict_rate_limit),
    path("geo-rate-limit", geographic_rate_limiting),
]
