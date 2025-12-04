from __future__ import annotations

from typing import NotRequired, TypedDict

from ..types import DateTimeString, ReadingTypeValue


class ReadingQuality(TypedDict, total=False):
    readingQualityType: NotRequired[str]


class IntervalReading(TypedDict, total=False):
    timestamp: NotRequired[DateTimeString]
    value: NotRequired[str]
    readingQualities: NotRequired[list[ReadingQuality]]


class IntervalBlock(TypedDict, total=False):
    readingType: NotRequired[ReadingTypeValue]
    intervalReadings: NotRequired[list[IntervalReading]]


class MeterReadings(TypedDict, total=False):
    usagePoint: NotRequired[str]
    messageCreated: NotRequired[DateTimeString]
    intervalBlocks: NotRequired[list[IntervalBlock]]
