import httpx
import pytest


@pytest.mark.asyncio
async def test_async_get_reading_types_requests_path(client_factory) -> None:
    captured: dict[str, httpx.Request] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json=[{"naziv": "Active Energy", "readingType": "1"}])

    client = client_factory(handler)
    reading_types = await client.aget_reading_types()

    assert captured["request"].url.path == "/reading-type"
    assert reading_types[0]["naziv"] == "Active Energy"
