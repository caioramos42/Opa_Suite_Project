from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.usuario import BodyList


class UsuarioContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de usuários."""
        self._url_path = manager.url_path if manager.url_path is not None else "usuario"
        self._manager = manager

    @Manager.make_request()
    def listar_usuarios(self, body: Optional[BodyList] = None) -> Any:
        """Lista usuários com filtros e paginação opcionais.

        Args:
            body: Filtros por nome, status e tipo, além da paginação. Se
                omitido, lista todos os usuários.

        Returns:
            Resposta JSON da API com os usuários encontrados.
        """
        return RequestModel(body=body)