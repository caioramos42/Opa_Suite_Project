from typing import Any, Optional
from dataclasses import field

from context.request.manager import Manager, RequestModel
from decorators.not_implemented import not_implemented_error
from decorators.dataclass_to_dict import dataclass_to_dict
from enums.methods import Actions


@dataclass_to_dict
class OptionsList:
    """Opções de paginação; ambos os valores são opcionais."""
    skip: Optional[int] = None
    limit: Optional[int] = None

@dataclass_to_dict
class Filter:
    """Filtros opcionais para a listagem de atendimentos."""
    protocolo: Optional[str] = None
    dataInicialAbertura: Optional[str] = None
    dataFinalAbertura: Optional[str] = None
    dataInicialEncerramento: Optional[str] = None
    dataFinalEncerramento: Optional[str] = None
    id_atendente: Optional[str] = field(
        default=None, metadata={"json_name": "id_atendente"}
    )
    status: Optional[str] = None
    canal_id: Optional[str] = field(default=None, metadata={"json_name": "canal_id"})
    setor: Optional[str] = None
    id_cliente: Optional[str] = field(default=None, metadata={"json_name": "id_cliente"})
    motivos_idMotivo: Optional[str] = None
    evaluations_ai_rating: Optional[str] = None
    evaluations_likert_rating: Optional[str] = None
    
@dataclass_to_dict
class BodyList:
    """Corpo da listagem: `filter` é obrigatório e `options` é opcional."""
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None

class AtendimentoContext():
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto usando o manager e a rota configurada."""
        self._url_path = manager.url_path if manager.url_path is not None else "atendimento"
        self._manager = manager

    @Manager.make_request()
    def buscar_atendimento_populado(self, id: str) -> RequestModel:
        """Busca um atendimento pelo ID, incluindo os dados relacionados.

        Args:
            id: Identificador do atendimento.

        Returns:
            Resposta JSON da API com o atendimento populado.
        """
        return RequestModel(url_data=id)
        
    @Manager.make_request()
    def listar_atendimentos(self, body: Optional[BodyList] = None) -> Any:
        """Lista atendimentos com filtros e paginação opcionais.

        Args:
            body: Filtros e opções de paginação. Sem filtros de data, a API
                considera os últimos 365 dias.

        Returns:
            Resposta JSON da API com os atendimentos encontrados.
        """
        return RequestModel(body=body)
    
    @not_implemented_error
    def criar_observacao(self, id_atendimento: str, message: str) -> None:
        """Cria uma observação no atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            message: Texto da observação.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...
    
    @not_implemented_error
    def adicionar_etiqueta(self, id_atendimento: str, tag_id: str) -> None:
        """Adiciona uma etiqueta ao atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            tag_id: Identificador da etiqueta.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...
    
    @not_implemented_error
    def adicionar_motivo(self, id_atendimento: str, reason_id: str) -> None:
        """Adiciona um motivo ao atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            reason_id: Identificador do motivo.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...
    
    @not_implemented_error
    def remover_etiqueta(self, id_atendimento: str, id_etiqueta: str) -> None:
        """Remove uma etiqueta do atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            id_etiqueta: Identificador da etiqueta.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...
    