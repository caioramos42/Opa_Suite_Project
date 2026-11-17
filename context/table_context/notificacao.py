from typing import Any

from context.request.manager import Manager
from decorators.not_implemented import not_implemented_error


class NotificacaoContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de notificações."""
        self._url_path = manager.url_path if manager.url_path is not None else "notificacao"
        self._manager = manager

    @not_implemented_error
    def enviar_notificacao(self, body: dict[str, Any]) -> None:
        """Envia uma notificação aos usuários do sistema.

        Args:
            body: Tipo, título, descrição e destinatários da notificação.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...