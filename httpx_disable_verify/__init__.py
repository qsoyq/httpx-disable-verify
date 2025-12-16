from typing import Callable
from functools import wraps

import httpx


class _PatchClient(httpx.Client):
    def __init__(self, *args, **kwargs):
        kwargs["verify"] = False
        super().__init__(*args, **kwargs)


class _PatchAsyncClient(httpx.AsyncClient):
    def __init__(self, *args, **kwargs):
        kwargs["verify"] = False
        super().__init__(*args, **kwargs)


def _patch_request(func: Callable):
    @wraps(func)
    def request(*args, **kwargs):
        kwargs["verify"] = False
        return func(*args, **kwargs)

    return request


def patch():
    ...
    httpx._api.request = _patch_request(httpx._api.request)
    httpx.Client = _PatchClient
    httpx.AsyncClient = _PatchAsyncClient


patch()
