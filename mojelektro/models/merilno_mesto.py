from __future__ import annotations

from typing import TYPE_CHECKING, NotRequired, TypedDict

from .common import (
    IdentifikatorMerilnegaMesta,
    PogodbeniPodatki,
    PoslovniPartner,
    TehnicniPodatki,
    TockaPrikljucitve,
)

if TYPE_CHECKING:
    from .merilna_tocka import MerilnaTocka


class MerilnoMesto(TypedDict, total=False):
    identifikator: NotRequired[IdentifikatorMerilnegaMesta]
    merilneTocke: NotRequired[list["MerilnaTocka"]]


class MerilnoMestoPolno(MerilnoMesto, total=False):
    naziv: NotRequired[str]
    naslov: NotRequired[str]
    tockaPrikljucitve: NotRequired[TockaPrikljucitve]
    pogodbeniPodatki: NotRequired[PogodbeniPodatki]
    lastnik: NotRequired[PoslovniPartner]
    tehnicniPodatki: NotRequired[TehnicniPodatki]
