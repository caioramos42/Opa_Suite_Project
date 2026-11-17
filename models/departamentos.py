from dataclasses import field
from typing import Optional

from decorators.dataclass_to_dict import dataclass_to_dict


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


@dataclass_to_dict
class DepartamentoBody:
    nome: str
    status: str
    tipo_encaminhamento_ligacoes: str = field(
        metadata={"json_name": "tipoEncaminhamentoLigacoes"}
    )
    token: Optional[str] = None
    ordem: Optional[int] = None
    parametros: Optional[list[str]] = None
    flow_avaliacao: Optional[str] = field(
        default=None, metadata={"json_name": "flowAvaliacao"}
    )
    encerramento_inatividade_avaliacao: Optional[int] = field(
        default=None,
        metadata={"json_name": "encerramentoInatividadeAvaliacao"},
    )
    mensagem_encerramento_inatividade: Optional[str] = field(
        default=None,
        metadata={"json_name": "mensagemEncerramentoInatividade"},
    )
    cod_pabx: Optional[str] = field(
        default=None, metadata={"json_name": "cod_pabx"}
    )
    departamento_transbordo_alternativo: Optional[str] = field(
        default=None,
        metadata={"json_name": "departamentoTransbordoAlternativo"},
    )
    encaminhar_ligacao: Optional[int] = field(
        default=None, metadata={"json_name": "encaminharLigacao"}
    )
    encerrar_atend_pabx_ao_desligar: Optional[bool] = field(
        default=None,
        metadata={"json_name": "encerrarAtendPabxAoDesligar"},
    )
