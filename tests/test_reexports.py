import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

import django

django.setup()


def test_all_exports_importable() -> None:
    import djangoapi_guard

    for name in djangoapi_guard.__all__:
        assert hasattr(djangoapi_guard, name), f"{name} not found"


def test_middleware_importable() -> None:
    from djangoapi_guard.middleware import DjangoAPIGuard

    assert DjangoAPIGuard is not None


def test_adapters_importable() -> None:
    from djangoapi_guard.adapters import (
        DjangoGuardRequest,
        DjangoGuardResponse,
        DjangoResponseFactory,
    )

    assert DjangoGuardRequest is not None
    assert DjangoGuardResponse is not None
    assert DjangoResponseFactory is not None
