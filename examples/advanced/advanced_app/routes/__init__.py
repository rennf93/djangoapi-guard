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

__all__ = [
    "access_urls",
    "admin_urls",
    "advanced_urls",
    "auth_urls",
    "basic_urls",
    "behavior_urls",
    "content_urls",
    "headers_urls",
    "health_urls",
    "rate_urls",
    "test_urls",
]
