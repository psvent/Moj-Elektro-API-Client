from __future__ import annotations

from dataclasses import dataclass

DEFAULT_BASE_URL = "https://api-test.informatika.si/mojelektro/v1"


@dataclass(slots=True)
class Config:
    """Configuration for Moj Elektro API access."""

    api_token: str
    base_url: str = DEFAULT_BASE_URL
    timeout: float = 10.0

    def __post_init__(self) -> None:
        if not self.api_token:
            raise ValueError("api_token is required")
        if not self.base_url:
            raise ValueError("base_url is required")

    def headers(self) -> dict[str, str]:
        return {"X-API-TOKEN": self.api_token}
