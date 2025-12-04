from __future__ import annotations

from enum import Enum
from typing import NewType

Gsrn = NewType("Gsrn", str)
ReadingTypeValue = NewType("ReadingTypeValue", str)
DateString = str
DateTimeString = str
DecimalString = str


class ReadingTypeValueType(str, Enum):
    KOLICINA = "KOLICINA"
    STANJE = "STANJE"


class VrstaMerilneTocke(str, Enum):
    OMTO = "OMTO"
    MTP = "MTP"


class NacinDolocitveDogovorjeneMoci(str, Enum):
    DISTRIBUTER = "DISTRIBUTER"
    UPORABNIK = "UPORABNIK"


class OznakaIzracunaDogovorjeneMoci(str, Enum):
    M0 = "M0"
    M1 = "M1"


class NacinObracuna(str, Enum):
    PREDVIDENA_PORABA = "PREDVIDENA_PORABA"
    DEJANSKA_PORABA = "DEJANSKA_PORABA"


__all__ = [
    "DateString",
    "DateTimeString",
    "DecimalString",
    "Gsrn",
    "NacinDolocitveDogovorjeneMoci",
    "NacinObracuna",
    "OznakaIzracunaDogovorjeneMoci",
    "ReadingTypeValue",
    "ReadingTypeValueType",
    "VrstaMerilneTocke",
]
