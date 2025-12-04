from __future__ import annotations

from typing import Any, Mapping


class MojElektroError(Exception):
    """Base error for the Moj Elektro client."""


class APIError(MojElektroError):
    """Represents an HTTP error response."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        error: Mapping[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error = error


class BadRequestError(APIError):
    """Raised for HTTP 400 responses."""


class AuthenticationError(APIError):
    """Raised for HTTP 401 responses."""


class AuthorizationError(APIError):
    """Raised for HTTP 403 responses."""


class NotFoundError(APIError):
    """Raised for HTTP 404 responses."""


class ResponseDecodingError(MojElektroError):
    """Raised when a response body cannot be decoded as JSON."""

    def __init__(self, message: str, *, body: bytes) -> None:
        super().__init__(message)
        self.body = body
