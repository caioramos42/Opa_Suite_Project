from dataclasses import field
from typing import Optional

from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    """Opções de paginação; ambos os valores são opcionais."""

    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    """Filtros opcionais para a listagem de atendimentos."""

    protocolo: Optional[str] = None
    dataInicialAbertura: Optional[str] = None
    dataFinalAbertura: Optional[str] = None
    dataInicialEncerramento: Optional[str] = None
    dataFinalEncerramento: Optional[str] = None
    id_atendente: Optional[str] = field(
        default=None, metadata={"json_name": "id_atendente"}
    )
    status: Optional[str] = None
    canal_id: Optional[str] = field(default=None, metadata={"json_name": "canal_id"})
    setor: Optional[str] = None
    id_cliente: Optional[str] = field(default=None, metadata={"json_name": "id_cliente"})
    motivos_idMotivo: Optional[str] = None
    evaluations_ai_rating: Optional[str] = None
    evaluations_likert_rating: Optional[str] = None


@dataclass_to_dict
class BodyList:
    """Filtros e opções de paginação para a listagem de atendimentos."""

    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


@dataclass_to_dict
class ObservacaoBody:
    message: str


@dataclass_to_dict
class EtiquetaAtendimentoBody:
    tag_id: str = field(metadata={"json_name": "tagId"})


@dataclass_to_dict
class MotivoAtendimentoBody:
    reason_id: str = field(metadata={"json_name": "reasonId"})
