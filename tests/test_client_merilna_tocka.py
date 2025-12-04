import httpx


def test_get_merilna_tocka_requests_path(client_factory) -> None:
    captured: dict[str, httpx.Request] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json={"gsrn": "gsrn-1", "dogovorjeneMoci": []})

    client = client_factory(handler)
    response = client.get_merilna_tocka("gsrn-1")

    assert captured["request"].url.path == "/merilna-tocka/gsrn-1"
    assert response["gsrn"] == "gsrn-1"
