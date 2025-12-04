from __future__ import annotations

from typing import NotRequired, TypedDict

from ..types import (
    DateString,
    DateTimeString,
    DecimalString,
    Gsrn,
    NacinDolocitveDogovorjeneMoci,
    NacinObracuna,
    OznakaIzracunaDogovorjeneMoci,
)


class Napaka(TypedDict, total=False):
    koda: str
    opis: str


class OpisNapake(TypedDict, total=False):
    zahteva: NotRequired[str]
    errors: NotRequired[list[Napaka]]


class PoslovniPartner(TypedDict, total=False):
    naziv: NotRequired[str]
    davcnaSt: NotRequired[str]
    maticnaSt: NotRequired[str]
    naslov: NotRequired[str]


class TockaPrikljucitve(TypedDict, total=False):
    rtp: NotRequired[str]
    sn: NotRequired[str]
    tp: NotRequired[str]
    nn: NotRequired[str]


class PogodbeniPodatki(TypedDict, total=False):
    stevilkaSzP: NotRequired[int]
    nazivNapetostnegaNivoja: NotRequired[str]
    oznakaNapetostnegaNivoja: NotRequired[str]
    nazivNacinaPrikljucitve: NotRequired[str]
    oznakaNacinaPrikljucitve: NotRequired[int]
    vrstaPrikljucka: NotRequired[str]
    steviloFaz: NotRequired[int]
    vrstaOmejevalcaToka: NotRequired[str]
    idVrsteOmejevalcaToka: NotRequired[int]
    jakostOmejevalcaToka: NotRequired[int]
    prikljucnaMoc: NotRequired[int]
    instaliranaMocProizvodnje: NotRequired[DecimalString]
    virPrimarnegaEnergenta: NotRequired[str]
    daljinskoCitanje: NotRequired[bool]
    obstoj15MinutneMeritve: NotRequired[bool]
    idFrekvenceOdbiranja: NotRequired[int]
    nazivFrekvenceOdbiranja: NotRequired[str]
    mesecObracuna: NotRequired[int]


class TehnicniPodatki(TypedDict, total=False):
    tipStevca: NotRequired[str]
    statisticnaPopulacija: NotRequired[str]
    tovarniskaStevilkaMkn: NotRequired[str]
    velikostPopulacije: NotRequired[int]
    letoIzdelave: NotRequired[int]
    zaporednaStPreizkusa: NotRequired[int]
    datumVeljavnostiZiga: NotRequired[DateString]


class IdentifikatorMerilnegaMesta(TypedDict, total=False):
    enotniIdentifikatorMerilnegaMesta: NotRequired[str]
    gsrn: NotRequired[Gsrn]


class DogovorjenaMoc(TypedDict, total=False):
    datumVnosa: NotRequired[DateString]
    datumOd: NotRequired[DateTimeString]
    datumDo: NotRequired[DateTimeString]
    nacinDolocitve: NotRequired[NacinDolocitveDogovorjeneMoci]
    oznakaIzracuna: NotRequired[OznakaIzracunaDogovorjeneMoci]
    casovniBlok1: NotRequired[DecimalString]
    casovniBlok2: NotRequired[DecimalString]
    casovniBlok3: NotRequired[DecimalString]
    casovniBlok4: NotRequired[DecimalString]
    casovniBlok5: NotRequired[DecimalString]
    veljavnost: NotRequired[bool]
    novUporabnik: NotRequired[bool]
    prikljucnaMoc: NotRequired[DecimalString]
    minimalnaMoc: NotRequired[DecimalString]


class Dobavitelj(TypedDict, total=False):
    oznaka: NotRequired[int]
    eic: NotRequired[str]
    naziv: NotRequired[str]
    datumOd: NotRequired[DateString]
    datumDo: NotRequired[DateString]


class NacinObracunaPodatki(TypedDict, total=False):
    nacinObracuna: NotRequired[NacinObracuna]
