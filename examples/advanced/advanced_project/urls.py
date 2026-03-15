import logging

from advanced_app.models import error_response
from advanced_app.routes.access_control import urlpatterns as access_urls
from advanced_app.routes.admin import urlpatterns as admin_urls
from advanced_app.routes.advanced import urlpatterns as advanced_urls
from advanced_app.routes.auth import urlpatterns as auth_urls
from advanced_app.routes.basic import urlpatterns as basic_urls
from advanced_app.routes.behavioral import urlpatterns as behavior_urls
from advanced_app.routes.content import urlpatterns as content_urls
from advanced_app.routes.headers import urlpatterns as headers_urls
from advanced_app.routes.health import urlpatterns as health_urls
from advanced_app.routes.rate_limiting import urlpatterns as rate_urls
from advanced_app.routes.testing import urlpatterns as test_urls
from django.http import HttpRequest, JsonResponse
from django.urls import include, path

logger = logging.getLogger(__name__)


def root(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        {
            "message": "DjangoAPI Guard Advanced Example API",
            "version": "1.0.0",
            "infrastructure": {
                "reverse_proxy": "nginx",
                "process_manager": "gunicorn",
                "cache": "redis",
            },
            "routes": {
                "/health": "Health checks",
                "/basic": "Basic security features",
                "/access": "Access control",
                "/auth": "Authentication examples",
                "/rate": "Rate limiting",
                "/behavior": "Behavioral analysis",
                "/headers": "Security headers",
                "/content": "Content filtering",
                "/advanced": "Advanced features",
                "/admin": "Admin utilities",
                "/test": "Security testing",
            },
        }
    )


def handler404_view(request: HttpRequest, exception: Exception) -> JsonResponse:
    return JsonResponse(error_response("Not found", "HTTP_404"), status=404)


def handler500_view(request: HttpRequest) -> JsonResponse:
    logger.error("Internal server error", exc_info=True)
    return JsonResponse(
        error_response("Internal server error", "INTERNAL_ERROR"), status=500
    )


urlpatterns = [
    path("", root),
    *health_urls,
    path("basic/", include((basic_urls, "basic"))),
    path("access/", include((access_urls, "access"))),
    path("auth/", include((auth_urls, "auth"))),
    path("rate/", include((rate_urls, "rate"))),
    path("behavior/", include((behavior_urls, "behavior"))),
    path("headers/", include((headers_urls, "headers"))),
    path("content/", include((content_urls, "content"))),
    path("advanced/", include((advanced_urls, "advanced"))),
    path("admin/", include((admin_urls, "admin"))),
    path("test/", include((test_urls, "test"))),
]

handler404 = "advanced_project.urls.handler404_view"
handler500 = "advanced_project.urls.handler500_view"
