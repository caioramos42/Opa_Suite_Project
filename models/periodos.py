from typing import Optional

from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    segunda: Optional[bool] = None
    terca: Optional[bool] = None
    quarta: Optional[bool] = None
    quinta: Optional[bool] = None
    sexta: Optional[bool] = None
    sabado: Optional[bool] = None
    domingo: Optional[bool] = None
    feriado: Optional[bool] = None
    nome: Optional[str] = None
    horaInicio: Optional[str] = None
    horaFim: Optional[str] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None
