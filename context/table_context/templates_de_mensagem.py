from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.templates_de_mensagem import BodyList, EnvioTemplateBody


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

    @Manager.make_request()
    def enviar_template(self, body: EnvioTemplateBody) -> Any:
        """Envia um template de mensagem a um contato.

        Args:
            body: Dados do contato, template e canal de envio.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(body=body)