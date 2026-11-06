# flake8: noqa

__all__ = [
    "ReviewApi",
    "StoreApi",
]

import typing as _typing

if _typing.TYPE_CHECKING:
    # import apis into api package
    from neurostore_sdk.api.review_api import ReviewApi
    from neurostore_sdk.api.store_api import StoreApi
    
else:
    from importlib import import_module

    _exports = {
        "ReviewApi": ".review_api",
        "StoreApi": ".store_api",
    }

    def __getattr__(name: str) -> object:
        if (module_name := _exports.get(name)) is None:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
        value = getattr(import_module(module_name, __name__), name)
        globals()[name] = value
        return value

    def __dir__() -> list[str]:
        return sorted(globals().keys() | _exports.keys())
