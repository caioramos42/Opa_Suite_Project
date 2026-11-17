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
    token: Optional[str] = None
    cod_pabx: Optional[str] = field(default=None, metadata={"json_name": "cod_pabx"})
    realizaAtendimento: Optional[bool] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


class DepartamentosContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de departamentos."""
        self._url_path = (
            manager.url_path
            if manager.url_path is not None
            else "departamento"
        )
        self._manager = manager

    @Manager.make_request()
    def listar_departamentos(self, body: Optional[BodyList] = None) -> Any:
        """Lista departamentos com filtros e paginação opcionais.

        Args:
            body: Filtros de departamento e opções de paginação. Se omitido,
                lista todos os departamentos.

        Returns:
            Resposta JSON da API com os departamentos encontrados.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def buscar_departamento_populado(self, id_departamento: str) -> RequestModel:
        """Busca um departamento pelo ID.

        Args:
            id_departamento: Identificador do departamento.

        Returns:
            Resposta JSON da API com os dados do departamento.
        """
        return RequestModel(url_data=id_departamento)

    @not_implemented_error
    def criar_departamento(self, body: dict[str, Any]) -> None:
        """Cria um departamento.

        Args:
            body: Dados do novo departamento.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...

    @not_implemented_error
    def editar_departamento(
        self, id_departamento: str, body: dict[str, Any]
    ) -> None:
        """Atualiza um departamento.

        Args:
            id_departamento: Identificador do departamento.
            body: Dados completos para atualização.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...