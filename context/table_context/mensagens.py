from typing import Any, Optional
from dataclasses import field

from context.request.manager import Manager, RequestModel
from decorators.dataclass_to_dict import dataclass_to_dict
from decorators.not_implemented import not_implemented_error

@dataclass_to_dict
class OptionsList:
    """Opções de paginação; ambos os valores são opcionais."""
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    """Filtros opcionais para a listagem de atendimentos."""
    id_rota: Optional[str] = field(default=None, metadata={"json_name": "id_rota"})
    
@dataclass_to_dict
class BodyList:
    """Corpo da listagem: `filter` é obrigatório e `options` é opcional."""

    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None

   
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

    @not_implemented_error
    def enviar_mensagem_em_atendimento_em_andamento(
        self, body: dict[str, Any]
    ) -> None:
        """Envia uma mensagem a um atendimento em andamento.

        Args:
            body: Payload com ``customerServiceId`` e ``content``.

        Raises:
            NotImplementedError: Esta rota ainda não foi implementada.
        """
        ...
    
        