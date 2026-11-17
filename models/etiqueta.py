from dataclasses import field
from typing import Optional

from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    nome: Optional[str] = None
    id_criador: Optional[str] = field(
        default=None, metadata={"json_name": "id_criador"}
    )
    empresa: Optional[str] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


@dataclass_to_dict
class CriarEtiquetaBody:
    nome: str
    cor: str
    tipo: str
    id_criador: Optional[str] = field(
        default=None, metadata={"json_name": "id_criador"}
    )
