from dataclasses import field
from typing import Any, Optional

from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    """Opções de paginação; ambos os valores são opcionais."""

    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    """Filtros opcionais para a listagem de atendimentos."""

    id_rota: Optional[str] = field(default=None, metadata={"json_name": "id_rota"})


@dataclass_to_dict
class BodyList:
    """Filtro e opções de paginação para listar mensagens."""

    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


@dataclass_to_dict
class MensagemEmAndamentoBody:
    content: dict[str, Any]
    customer_service_id: str = field(
        metadata={"json_name": "customerServiceId"}
    )
