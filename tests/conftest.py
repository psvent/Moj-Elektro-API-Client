from __future__ import annotations

from collections.abc import Callable

import httpx
import pytest

from mojelektro import Config, MojElektroClient
from mojelektro._http import HTTPClient


@pytest.fixture
def config() -> Config:
    return Config(api_token="test-token", base_url="https://api.test")


@pytest.fixture
def client_factory(config: Config):
    def _make(handler: Callable[[httpx.Request], httpx.Response]) -> MojElektroClient:
        transport = httpx.MockTransport(handler)
        http_client = HTTPClient(config, transport=transport)
        return MojElektroClient(config, http_client=http_client)

    return _make
