from __future__ import annotations

from typing import NotRequired, TypedDict

from ..types import ReadingTypeValue, ReadingTypeValueType


class ReadingType(TypedDict, total=False):
    naziv: NotRequired[str]
    oznaka: NotRequired[str]
    tip: NotRequired[str]
    perioda: NotRequired[str]
    opis: NotRequired[str]
    readingType: NotRequired[ReadingTypeValue]
    readingTypeBrezObracuna: NotRequired[ReadingTypeValue]
    readingTypeObracun: NotRequired[ReadingTypeValue]
    vrsta: NotRequired[ReadingTypeValueType]


ReadingTypes = list[ReadingType]
