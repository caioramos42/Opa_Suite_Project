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
    id_criador: Optional[str] = field(
        default=None, metadata={"json_name": "id_criador"}
    )
    empresa: Optional[str] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


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

    @not_implemented_error
    def criar_etiqueta(self, body: dict[str, Any]) -> None:
        """Cria uma etiqueta.

        Args:
            body: Dados da etiqueta, como nome, cor e tipo.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...