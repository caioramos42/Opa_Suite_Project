from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.cliente import (
    BodyList,
    ClienteBody,
    ClientePatchBody,
)


class ClienteContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de clientes."""
        self._url_path = manager.url_path if manager.url_path is not None else "cliente"
        self._manager = manager

    @Manager.make_request()
    def listar_clientes(self, body: Optional[BodyList] = None) -> Any:
        """Lista clientes com filtros e paginação opcionais.

        Args:
            body: Filtros de cliente e opções de paginação. Se omitido, lista
                todos os clientes.

        Returns:
            Resposta JSON da API com os clientes encontrados.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def buscar_cliente_populado(self, id_cliente: str) -> RequestModel:
        """Busca um cliente pelo ID.

        Args:
            id_cliente: Identificador do cliente.

        Returns:
            Resposta JSON da API com os dados do cliente.
        """
        return RequestModel(url_data=id_cliente)

    @Manager.make_request()
    def criar_cliente(self, body: ClienteBody) -> Any:
        """Cria um cliente.

        Args:
            body: Dados do cliente a serem enviados.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def editar_cliente(self, id_cliente: str, body: ClienteBody) -> Any:
        """Substitui os dados de um cliente.

        Args:
            id_cliente: Identificador do cliente.
            body: Dados completos que serão enviados para atualização.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(url_data=id_cliente, body=body)

    @Manager.make_request()
    def editar_parcialmente_cliente(
        self, id_cliente: str, body: ClientePatchBody
    ) -> Any:
        """Atualiza parcialmente os dados de um cliente.

        Args:
            id_cliente: Identificador do cliente.
            body: Campos que serão alterados.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(url_data=id_cliente, body=body)

    @Manager.make_request()
    def remover_cliente(self, id_cliente: str) -> Any:
        """Remove um cliente que ainda não tenha atendimentos.

        Args:
            id_cliente: Identificador do cliente.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(url_data=id_cliente)