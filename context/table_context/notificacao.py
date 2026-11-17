from typing import Any

from context.request.manager import Manager, RequestModel
from models.notificacao import NotificacaoBody


class NotificacaoContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de notificações."""
        self._url_path = manager.url_path if manager.url_path is not None else "notificacao"
        self._manager = manager

    @Manager.make_request()
    def enviar_notificacao(self, body: NotificacaoBody) -> Any:
        """Envia uma notificação aos usuários do sistema.

        Args:
            body: Tipo, título, descrição e destinatários da notificação.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(body=body)