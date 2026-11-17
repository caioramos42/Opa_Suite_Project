from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    motivo: Optional[str] = None
    departamentos: Optional[str] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


class MotivosContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de motivos de atendimento."""
        self._url_path = manager.url_path if manager.url_path is not None else "motivo"
        self._manager = manager

    @Manager.make_request()
    def listar_motivos(self, body: Optional[BodyList] = None) -> Any:
        """Lista motivos com filtros e paginação opcionais.

        Args:
            body: Filtros por motivo/departamento e opções de paginação. Se
                omitido, lista todos os motivos.

        Returns:
            Resposta JSON da API com os motivos encontrados.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def buscar_motivo(self, id_motivo: str) -> RequestModel:
        """Busca um motivo de atendimento pelo ID.

        Args:
            id_motivo: Identificador do motivo.

        Returns:
            Resposta JSON da API com os dados do motivo.
        """
        return RequestModel(url_data=id_motivo)