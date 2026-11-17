from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.contatos import BodyList, ContatoBody


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

    @Manager.make_request()
    def criar_contato(self, body: ContatoBody) -> Any:
        """Cria um contato.

        Args:
            body: Dados de identificação e contato.

        Returns:
            Resposta JSON da API.
        """
        if body.senha is None or body.repetir_senha is None:
            raise ValueError(
                "Informe senha e repetir_senha para criar um contato."
            )
        return RequestModel(body=body)

    @Manager.make_request()
    def editar_contato(self, id_contato: str, body: ContatoBody) -> Any:
        """Atualiza os dados de um contato.

        Args:
            id_contato: Identificador do contato.
            body: Dados completos para atualização.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(url_data=id_contato, body=body)

    @Manager.make_request()
    def remover_contato(self, id_contato: str) -> Any:
        """Remove um contato que ainda não tenha realizado atendimentos.

        Args:
            id_contato: Identificador do contato.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(url_data=id_contato)