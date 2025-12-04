from __future__ import annotations

from typing import NotRequired, TypedDict


class ReadingQuality(TypedDict, total=False):
    readingQualityType: NotRequired[str]


class ReadingQualityWithDescription(ReadingQuality, total=False):
    description: NotRequired[str]


ReadingQualities = list[ReadingQualityWithDescription]
