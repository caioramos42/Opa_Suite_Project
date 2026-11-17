from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.etiqueta import BodyList, CriarEtiquetaBody


class EtiquetaContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de etiquetas."""
        self._url_path = manager.url_path if manager.url_path is not None else "etiqueta"
        self._manager = manager

    @Manager.make_request()
    def listar_etiquetas(self, body: Optional[BodyList] = None) -> Any:
        """Lista etiquetas com filtros e paginação opcionais.

        Args:
            body: Filtros de etiqueta e opções de paginação. Se omitido, lista
                todas as etiquetas.

        Returns:
            Resposta JSON da API com as etiquetas encontradas.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def criar_etiqueta(self, body: CriarEtiquetaBody) -> Any:
        """Cria uma etiqueta.

        Args:
            body: Dados da etiqueta, como nome, cor e tipo.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(body=body)