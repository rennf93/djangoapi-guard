from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_GET

from advanced_app.models import health_response


@require_GET
def health_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse(health_response("healthy"))


@require_GET
def readiness_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse(health_response("ready"))


urlpatterns = [
    path("health", health_check),
    path("ready", readiness_check),
]
