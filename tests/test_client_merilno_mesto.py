import httpx


def test_get_merilno_mesto_requests_path(client_factory) -> None:
    captured: dict[str, httpx.Request] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json={"naziv": "Lokacija", "merilneTocke": []})

    client = client_factory(handler)
    response = client.get_merilno_mesto("identifier-1")

    assert captured["request"].url.path == "/merilno-mesto/identifier-1"
    assert response["naziv"] == "Lokacija"
