import httpx
import pytest

from mojelektro import (
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    NotFoundError,
    ResponseDecodingError,
)


def test_bad_request_error_includes_payload(client_factory) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={"koda": "E.7.155", "opis": "invalid"})

    client = client_factory(handler)

    with pytest.raises(BadRequestError) as exc:
        client.get_reading_types()

    assert exc.value.status_code == 400
    assert exc.value.error == {"koda": "E.7.155", "opis": "invalid"}


def test_auth_errors_are_mapped(client_factory) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"opis": "missing token"})

    client = client_factory(handler)
    with pytest.raises(AuthenticationError):
        client.get_merilno_mesto("id-1")

    def handler_forbidden(request: httpx.Request) -> httpx.Response:
        return httpx.Response(403, json={"opis": "not allowed"})

    client = client_factory(handler_forbidden)
    with pytest.raises(AuthorizationError):
        client.get_merilna_tocka("gsrn-1")


def test_not_found_and_decoding_errors(client_factory) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"opis": "not found"})

    client = client_factory(handler)
    with pytest.raises(NotFoundError):
        client.get_reading_qualities()

    def invalid_json(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"not-json")

    client = client_factory(invalid_json)
    with pytest.raises(ResponseDecodingError):
        client.get_reading_types()
