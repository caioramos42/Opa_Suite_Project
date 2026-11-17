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
    atalho: Optional[str] = None
    tipo_mensagem: Optional[str] = field(
        default=None, metadata={"json_name": "tipo_mensagem"}
    )


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


class TemplateDeMensagemContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de templates de mensagem."""
        self._url_path = manager.url_path if manager.url_path is not None else "template"
        self._manager = manager

    @Manager.make_request()
    def listar_templates(
        self, body: Optional[BodyList] = None
    ) -> Any:
        """Lista templates de mensagem com filtros e paginação opcionais.

        Args:
            body: Filtro por atalho/tipo e opções de paginação. Se omitido,
                lista todos os templates.

        Returns:
            Resposta JSON da API com os templates encontrados.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def buscar_template_populado(self, id_template: str) -> RequestModel:
        """Busca um template pelo ID, incluindo os dados relacionados.

        Args:
            id_template: Identificador do template.

        Returns:
            Resposta JSON da API com o template populado.
        """
        return RequestModel(url_data=id_template)

    @not_implemented_error
    def enviar_template(self, body: dict[str, Any]) -> None:
        """Envia um template de mensagem a um contato.

        Args:
            body: Dados do contato, template e canal de envio.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...