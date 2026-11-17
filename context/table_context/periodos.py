from typing import Any, Optional

from context.request.manager import Manager, RequestModel
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


class PeriodosContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de períodos de atendimento."""
        self._url_path = (
            manager.url_path
            if manager.url_path is not None
            else "atendimento/periodo"
        )
        self._manager = manager

    @Manager.make_request()
    def listar_periodos(self, body: Optional[BodyList] = None) -> Any:
        """Lista períodos de atendimento com filtros e paginação opcionais.

        Args:
            body: Filtros por dias, horário e nome, além das opções de
                paginação. Se omitido, lista todos os períodos.

        Returns:
            Resposta JSON da API com os períodos encontrados.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def buscar_periodo(self, id_periodo: str) -> RequestModel:
        """Busca um período de atendimento pelo ID.

        Args:
            id_periodo: Identificador do período.

        Returns:
            Resposta JSON da API com os dados do período.
        """
        return RequestModel(url_data=id_periodo)