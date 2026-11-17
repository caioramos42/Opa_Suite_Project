from dataclasses import field
from typing import Any, Optional

from context.request.manager import Manager, RequestModel
from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    nome: Optional[str] = None
    id_atendente: Optional[str] = field(
        default=None, metadata={"json_name": "id_atendente"}
    )
    status: Optional[str] = None
    canal: Optional[str] = None
    integracao: Optional[str] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


class CanaisDeComunicacaoContext:
    def __init__(self, manager: Manager) -> None:
        """Inicializa o contexto dos endpoints de canais de comunicação."""
        self._url_path = (
            manager.url_path
            if manager.url_path is not None
            else "canal-comunicacao"
        )
        self._manager = manager
    
    @Manager.make_request()
    def listar_canais_de_comunicacao(
        self, body: Optional[BodyList] = None
    ) -> Any:
        """Lista canais de comunicação conforme filtros e paginação.

        Args:
            body: Filtros de canal e opções de paginação. Se omitido, lista
                todos os canais.

        Returns:
            Resposta JSON da API com os canais encontrados.
        """
        return RequestModel(body=body)
    
    @Manager.make_request()
    def buscar_canal_de_comunicacao_populado(self, id_canal: str) -> RequestModel:
        """Busca um canal pelo ID, incluindo dados relacionados.

        Args:
            id_canal: Identificador do canal.

        Returns:
            Resposta JSON da API com o canal populado.
        """
        return RequestModel(url_data=id_canal)
    
    @Manager.make_request()
    def buscar_os_templates_de_mensagem_por_canal(self, id_canal: str) -> RequestModel:
        """Lista os templates de mensagem associados a um canal.

        Args:
            id_canal: Identificador do canal.

        Returns:
            Resposta JSON da API com os templates do canal.
        """
        return RequestModel(url_data=f"{id_canal}/template")
    
    @Manager.make_request()
    def buscar_limites_diarios_de_envio_de_templates_de_mensagem(
        self, id_canal: str
    ) -> RequestModel:
        """Consulta os limites diários de envio de templates do canal.

        Args:
            id_canal: Identificador do canal.

        Returns:
            Resposta JSON da API com os limites diários de envio.
        """
        return RequestModel(
            url_data=f"{id_canal}/template/limites-diarios-envio"
        )