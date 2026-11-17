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
    nome: Optional[str] = None
    email_principal: Optional[str] = field(
        default=None, metadata={"json_name": "email_principal"}
    )
    fones_numero: Optional[str] = None
    classificacao: Optional[str] = None
    cli_emp: Optional[str] = field(default=None, metadata={"json_name": "cli_emp"})


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


class ContatosContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de contatos."""
        self._url_path = manager.url_path if manager.url_path is not None else "contato"
        self._manager = manager

    @Manager.make_request()
    def listar_contatos(self, body: Optional[BodyList] = None) -> Any:
        """Lista contatos com filtros e paginação opcionais.

        Args:
            body: Filtros de contato e opções de paginação. Se omitido, lista
                todos os contatos.

        Returns:
            Resposta JSON da API com os contatos encontrados.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def buscar_contato_populado(self, id_contato: str) -> RequestModel:
        """Busca um contato pelo ID.

        Args:
            id_contato: Identificador do contato.

        Returns:
            Resposta JSON da API com os dados do contato.
        """
        return RequestModel(url_data=id_contato)

    @not_implemented_error
    def criar_contato(self, body: dict[str, Any]) -> None:
        """Cria um contato.

        Args:
            body: Dados de identificação e contato.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...

    @not_implemented_error
    def editar_contato(self, id_contato: str, body: dict[str, Any]) -> None:
        """Atualiza os dados de um contato.

        Args:
            id_contato: Identificador do contato.
            body: Dados completos para atualização.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...

    @not_implemented_error
    def remover_contato(self, id_contato: str) -> None:
        """Remove um contato que ainda não tenha realizado atendimentos.

        Args:
            id_contato: Identificador do contato.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...