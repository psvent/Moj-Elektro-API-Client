import httpx


def test_get_reading_qualities_requests_path(client_factory) -> None:
    captured: dict[str, httpx.Request] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(
            200,
            json=[{"readingQualityType": "quality", "description": "desc"}],
        )

    client = client_factory(handler)
    qualities = client.get_reading_qualities()

    assert captured["request"].url.path == "/reading-qualities"
    assert qualities[0]["readingQualityType"] == "quality"
