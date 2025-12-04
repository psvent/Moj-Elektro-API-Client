from __future__ import annotations

from typing import Any, Mapping, Sequence, cast

from ._http import HTTPClient
from .config import Config
from .models import (
    MerilnaTockaPolno,
    MerilnoMestoPolno,
    MeterReadings,
    ReadingQualities,
    ReadingTypes,
)


class MojElektroClient:
    """Public API surface for interacting with Moj Elektro."""

    def __init__(
        self,
        config: Config,
        *,
        http_client: HTTPClient | None = None,
    ) -> None:
        self.config = config
        self._http = http_client or HTTPClient(config)

    def get_meter_readings(
        self,
        *,
        usage_point: str,
        start_time: str,
        end_time: str,
        option: Sequence[str] | None = None,
    ) -> MeterReadings:
        params: Mapping[str, Any] = {
            "usagePoint": usage_point,
            "startTime": start_time,
            "endTime": end_time,
        }
        if option:
            params = {**params, "option": list(option)}
        response = self._http.get("meter-readings", params=params)
        return cast(MeterReadings, response)

    async def aget_meter_readings(
        self,
        *,
        usage_point: str,
        start_time: str,
        end_time: str,
        option: Sequence[str] | None = None,
    ) -> MeterReadings:
        params: Mapping[str, Any] = {
            "usagePoint": usage_point,
            "startTime": start_time,
            "endTime": end_time,
        }
        if option:
            params = {**params, "option": list(option)}
        response = await self._http.aget("meter-readings", params=params)
        return cast(MeterReadings, response)

    def get_merilno_mesto(self, identifikator: str) -> MerilnoMestoPolno:
        response = self._http.get(f"merilno-mesto/{identifikator}")
        return cast(MerilnoMestoPolno, response)

    async def aget_merilno_mesto(self, identifikator: str) -> MerilnoMestoPolno:
        response = await self._http.aget(f"merilno-mesto/{identifikator}")
        return cast(MerilnoMestoPolno, response)

    def get_merilna_tocka(self, gsrn: str) -> MerilnaTockaPolno:
        response = self._http.get(f"merilna-tocka/{gsrn}")
        return cast(MerilnaTockaPolno, response)

    async def aget_merilna_tocka(self, gsrn: str) -> MerilnaTockaPolno:
        response = await self._http.aget(f"merilna-tocka/{gsrn}")
        return cast(MerilnaTockaPolno, response)

    def get_reading_qualities(self) -> ReadingQualities:
        response = self._http.get("reading-qualities")
        return cast(ReadingQualities, response)

    async def aget_reading_qualities(self) -> ReadingQualities:
        response = await self._http.aget("reading-qualities")
        return cast(ReadingQualities, response)

    def get_reading_types(self) -> ReadingTypes:
        response = self._http.get("reading-type")
        return cast(ReadingTypes, response)

    async def aget_reading_types(self) -> ReadingTypes:
        response = await self._http.aget("reading-type")
        return cast(ReadingTypes, response)
