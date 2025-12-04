from __future__ import annotations

from typing import TYPE_CHECKING, NotRequired, TypedDict

from ..types import Gsrn, NacinObracuna, VrstaMerilneTocke
from .common import DogovorjenaMoc, Dobavitelj, PoslovniPartner

if TYPE_CHECKING:
    from .merilno_mesto import MerilnoMesto


class MerilnaTocka(TypedDict, total=False):
    gsrn: NotRequired[Gsrn]
    vrsta: NotRequired[VrstaMerilneTocke]


class MerilnaTockaPolno(MerilnaTocka, total=False):
    naziv: NotRequired[str]
    dobavitelj: NotRequired[Dobavitelj]
    obracunIzgub: NotRequired[bool]
    procentIzgub: NotRequired[int]
    steviloTarifMerjenja: NotRequired[int]
    letneObratovalneUre: NotRequired[int]
    placnikAliProdajalec: NotRequired[PoslovniPartner]
    naslovnik: NotRequired[PoslovniPartner]
    obracunskaMoc: NotRequired[int]
    nacinObracuna: NotRequired[NacinObracuna]
    idVrstaOdjema: NotRequired[int]
    nazivVrstaOdjema: NotRequired[str]
    stPogodbeOUporabiSistema: NotRequired[str]
    nacinOskrbe: NotRequired[str]
    dogovorjeneMoci: NotRequired[list[DogovorjenaMoc]]
    uporabniskaSkupina: NotRequired[str]
    tehnicnaVezalnaShema: NotRequired[str]
    obracunskaVezalnaShema: NotRequired[str]
    merilnaMesta: NotRequired[list["MerilnoMesto"]]
