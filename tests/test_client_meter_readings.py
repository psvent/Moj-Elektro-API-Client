import httpx


def test_get_meter_readings_builds_query(client_factory) -> None:
    captured: dict[str, httpx.Request] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(
            200,
            json={
                "usagePoint": "123",
                "messageCreated": "2024-01-01T00:00:00Z",
                "intervalBlocks": [],
            },
        )

    client = client_factory(handler)
    result = client.get_meter_readings(
        usage_point="123",
        start_time="2024-01-01",
        end_time="2024-01-02",
        option=["ReadingType=1", "ReadingType=2"],
    )

    request = captured["request"]
    assert request.url.path == "/meter-readings"
    assert request.url.params["usagePoint"] == "123"
    assert request.url.params["startTime"] == "2024-01-01"
    assert request.url.params.get_list("option") == ["ReadingType=1", "ReadingType=2"]
    assert result["usagePoint"] == "123"
