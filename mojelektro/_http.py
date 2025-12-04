from __future__ import annotations

from typing import Any, Mapping

import httpx

from .config import Config
from .exceptions import (
    APIError,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    NotFoundError,
    ResponseDecodingError,
)
from .models import Napaka


class HTTPClient:
    """Lightweight wrapper around httpx with Moj Elektro defaults."""

    def __init__(
        self,
        config: Config,
        *,
        timeout: float | None = None,
        transport: httpx.BaseTransport | None = None,
        client: httpx.Client | None = None,
        async_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.config = config
        self.timeout = timeout or config.timeout
        self.transport = transport
        self._client = client
        self._async_client = async_client

    def get(self, path: str, params: Mapping[str, Any] | None = None) -> Any:
        response = self._send_sync("GET", path, params=params)
        return self._handle_response(response)

    async def aget(self, path: str, params: Mapping[str, Any] | None = None) -> Any:
        response = await self._send_async("GET", path, params=params)
        return self._handle_response(response)

    def _send_sync(
        self, method: str, path: str, params: Mapping[str, Any] | None = None
    ) -> httpx.Response:
        close_client = False
        client = self._client
        if client is None:
            client = httpx.Client(
                base_url=self.config.base_url,
                headers=self.config.headers(),
                timeout=self.timeout,
                transport=self.transport,
            )
            close_client = True

        try:
            return client.request(method, path, params=params)
        finally:
            if close_client:
                client.close()

    async def _send_async(
        self, method: str, path: str, params: Mapping[str, Any] | None = None
    ) -> httpx.Response:
        close_client = False
        client = self._async_client
        if client is None:
            client = httpx.AsyncClient(
                base_url=self.config.base_url,
                headers=self.config.headers(),
                timeout=self.timeout,
                transport=self.transport,
            )
            close_client = True

        try:
            return await client.request(method, path, params=params)
        finally:
            if close_client:
                await client.aclose()

    def _handle_response(self, response: httpx.Response) -> Any:
        if response.status_code >= 400:
            self._raise_for_status(response)

        if response.status_code == 204:
            return None

        try:
            return response.json()
        except ValueError as exc:
            raise ResponseDecodingError(
                "Unable to decode response as JSON", body=response.content
            ) from exc

    def _raise_for_status(self, response: httpx.Response) -> None:
        error_body: Napaka | Mapping[str, Any] | None = None
        message = f"HTTP {response.status_code}"
        try:
            decoded = response.json()
            if isinstance(decoded, Mapping):
                error_body = decoded
                message = decoded.get("opis", message)
        except ValueError:
            # Keep the default message if the body is not JSON.
            pass

        status = response.status_code
        if status == 400:
            raise BadRequestError(message, status_code=status, error=error_body)
        if status == 401:
            raise AuthenticationError(message, status_code=status, error=error_body)
        if status == 403:
            raise AuthorizationError(message, status_code=status, error=error_body)
        if status == 404:
            raise NotFoundError(message, status_code=status, error=error_body)

        raise APIError(message, status_code=status, error=error_body)
