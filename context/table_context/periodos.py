from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.periodos import BodyList


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