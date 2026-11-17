from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.atendimento import (
    BodyList,
    EtiquetaAtendimentoBody,
    MotivoAtendimentoBody,
    ObservacaoBody,
)


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
    
    @Manager.make_request()
    def criar_observacao(
        self, id_atendimento: str, body: ObservacaoBody
    ) -> Any:
        """Cria uma observação no atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            body: Modelo com o texto da observação.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(
            url_data=f"{id_atendimento}/observacao",
            body=body,
        )
    
    @Manager.make_request()
    def adicionar_etiqueta(
        self, id_atendimento: str, body: EtiquetaAtendimentoBody
    ) -> Any:
        """Adiciona uma etiqueta ao atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            body: Modelo com o identificador da etiqueta.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(
            url_data=f"{id_atendimento}/etiqueta",
            body=body,
        )
    
    @Manager.make_request()
    def adicionar_motivo(
        self, id_atendimento: str, body: MotivoAtendimentoBody
    ) -> Any:
        """Adiciona um motivo ao atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            body: Modelo com o identificador do motivo.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(
            url_data=f"{id_atendimento}/motivo",
            body=body,
        )
    
    @Manager.make_request()
    def remover_etiqueta(self, id_atendimento: str, id_etiqueta: str) -> Any:
        """Remove uma etiqueta do atendimento.

        Args:
            id_atendimento: Identificador do atendimento.
            id_etiqueta: Identificador da etiqueta.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(
            url_data=f"{id_atendimento}/etiqueta/{id_etiqueta}"
        )
    