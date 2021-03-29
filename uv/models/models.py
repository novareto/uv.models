from pydantic import BaseModel, validator, Field
from typing import List, Optional
from datetime import date, time
from enum import Enum, IntEnum


class GeschlechtEnum(IntEnum):
    männlich = 1
    weiblich = 2


def construct_datum(v):
    if v.get('day') and v.get('month') and v.get('year'):
        return date(v.get('year'), v.get('month'), v.get('day'))
    return

def construct_zeit(v):
    if v.get('hour'):
        return time(v.get('hour'), v.get('minute'), v.get('second'))
    return

class VersichertePerson(BaseModel):

    nachname: str
    vorname: str
    strasse: str
    postleitzahl: str
    ort: str
    vorwahl: Optional[str]
    telefonnummer: Optional[str]
    geschlechtKNZ: str
    anredezeile: str
    personID: int
    titel: str = ""
    geburtsdatum: Optional[date]
    geschlechtKNZ: GeschlechtEnum

    _normalize_geburtsdatum = validator('geburtsdatum', pre=True, allow_reuse=True)(construct_datum)

    @validator('*', pre=True)
    def strip_strings(cls, v):
        if isinstance(v, str):
            return v.strip()
        return v


class VersichertenFall(BaseModel):
    aktenzeichen: str
    artDerPersonID: int
    artDerPersonKNZ: int
    artDerPersonPrompt: str
    artHeilverfahrenKNZ: str
    artHeilverfahrenPrompt: str
    bearbstsPrompt: str
    bezirksverwaltungPrompt: str
    bezirksverwaltungKNZ: int
    krankenkasseIKNummer: int
    krankenkassenTypPrompt: str
    sachbearbeiter: str
    personID: int
    mitgliedsnummer: int
    unfalldatum: Optional[date]
    unfallzeit: Optional[time]

    _normalize_unfalldatum = validator('unfalldatum', pre=True, allow_reuse=True)(construct_datum)
    _normalize_unfallzeit = validator('unfallzeit', pre=True, allow_reuse=True)(construct_zeit)


class Unternehmen(BaseModel):
    name1: str
    name2: str
    name3: Optional[str]
    strasse: str
    plz: str
    ort: str
