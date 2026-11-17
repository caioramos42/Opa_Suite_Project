from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.departamentos import BodyList, DepartamentoBody


class DepartamentosContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de departamentos."""
        self._url_path = (
            manager.url_path
            if manager.url_path is not None
            else "departamento"
        )
        self._manager = manager

    @Manager.make_request()
    def listar_departamentos(self, body: Optional[BodyList] = None) -> Any:
        """Lista departamentos com filtros e paginação opcionais.

        Args:
            body: Filtros de departamento e opções de paginação. Se omitido,
                lista todos os departamentos.

        Returns:
            Resposta JSON da API com os departamentos encontrados.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def buscar_departamento_populado(self, id_departamento: str) -> RequestModel:
        """Busca um departamento pelo ID.

        Args:
            id_departamento: Identificador do departamento.

        Returns:
            Resposta JSON da API com os dados do departamento.
        """
        return RequestModel(url_data=id_departamento)

    @Manager.make_request()
    def criar_departamento(self, body: DepartamentoBody) -> Any:
        """Cria um departamento.

        Args:
            body: Dados do novo departamento.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def editar_departamento(
        self, id_departamento: str, body: DepartamentoBody
    ) -> Any:
        """Atualiza um departamento.

        Args:
            id_departamento: Identificador do departamento.
            body: Dados completos para atualização.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(url_data=id_departamento, body=body)