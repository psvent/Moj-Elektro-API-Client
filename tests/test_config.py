import pytest

from mojelektro import Config, DEFAULT_BASE_URL


def test_config_defaults() -> None:
    cfg = Config(api_token="abc123")
    assert cfg.base_url == DEFAULT_BASE_URL
    assert cfg.timeout == 10.0
    assert cfg.headers()["X-API-TOKEN"] == "abc123"


def test_config_requires_token() -> None:
    with pytest.raises(ValueError):
        Config(api_token="")
