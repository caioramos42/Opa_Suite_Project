from dataclasses import field
from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from decorators.dataclass_to_dict import dataclass_to_dict
from decorators.not_implemented import not_implemented_error


@dataclass_to_dict
class OptionsList:
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    id: Optional[str] = None
    id_fornecedor: Optional[str] = field(
        default=None, metadata={"json_name": "id_fornecedor"}
    )
    id_filial: Optional[str] = field(
        default=None, metadata={"json_name": "id_filial"}
    )
    nome: Optional[str] = None
    fantasia: Optional[str] = None
    cpf_cnpj: Optional[str] = field(default=None, metadata={"json_name": "cpf_cnpj"})
    status: Optional[str] = None
    prospect: Optional[bool] = None
    cliente: Optional[bool] = None
    fornecedor: Optional[bool] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


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

    @not_implemented_error
    def criar_cliente(self, body: dict[str, Any]) -> None:
        """Cria um cliente.

        Args:
            body: Dados do cliente, incluindo nome e status.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...

    @not_implemented_error
    def editar_cliente(self, id_cliente: str, body: dict[str, Any]) -> None:
        """Substitui os dados de um cliente.

        Args:
            id_cliente: Identificador do cliente.
            body: Dados completos que serão enviados para atualização.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...

    @not_implemented_error
    def editar_parcialmente_cliente(
        self, id_cliente: str, body: dict[str, Any]
    ) -> None:
        """Atualiza parcialmente os dados de um cliente.

        Args:
            id_cliente: Identificador do cliente.
            body: Campos que serão alterados.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...

    @not_implemented_error
    def remover_cliente(self, id_cliente: str) -> None:
        """Remove um cliente que ainda não tenha atendimentos.

        Args:
            id_cliente: Identificador do cliente.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...