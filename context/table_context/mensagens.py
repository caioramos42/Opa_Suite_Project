from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from models.mensagens import BodyList, MensagemEmAndamentoBody


class MensagensContext():
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de mensagens."""
        self._url_path = (
            manager.url_path
            if manager.url_path is not None
            else "atendimento/mensagem"
        )
        self._manager = manager
        
    @Manager.make_request()
    def buscar_mensagem_atendimento_pupulada(self, id: str) -> RequestModel:
        """Busca uma mensagem pelo ID, incluindo os dados relacionados.

        Args:
            id: Identificador da mensagem.

        Returns:
            Resposta JSON da API com a mensagem populada.
        """
        return RequestModel(url_data=id)
    
    @Manager.make_request()
    def listar_mensagens_atendimento(self, body: Optional[BodyList] = None) -> Any:
        """Lista mensagens de atendimento com filtros e paginação opcionais.

        Args:
            body: Filtro por rota e opções de paginação. Se omitido, a API
                retorna todas as mensagens.

        Returns:
            Resposta JSON da API com as mensagens encontradas.
        """
        return RequestModel(body=body)

    @Manager.make_request()
    def enviar_mensagem_em_atendimento_em_andamento(
        self, body: MensagemEmAndamentoBody
    ) -> Any:
        """Envia uma mensagem a um atendimento em andamento.

        Args:
            body: Payload com o ID do atendimento e o conteúdo da mensagem.

        Returns:
            Resposta JSON da API.
        """
        return RequestModel(body=body)