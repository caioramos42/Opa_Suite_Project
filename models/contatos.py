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
    email_principal: Optional[str] = field(
        default=None, metadata={"json_name": "email_principal"}
    )
    fones_numero: Optional[str] = None
    classificacao: Optional[str] = None
    cli_emp: Optional[str] = field(default=None, metadata={"json_name": "cli_emp"})


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


@dataclass_to_dict
class ContatoBody:
    nome: str
    lead: bool
    requer_autenticacao_sempre: bool = field(
        metadata={"json_name": "requerAutenticacaoSempre"}
    )
    habilitar_alerta: bool = field(metadata={"json_name": "habilitarAlerta"})
    historico_email: bool = field(metadata={"json_name": "historico_email"})
    celular_completo: Optional[str] = field(
        default=None, metadata={"json_name": "celularCompleto"}
    )
    senha: Optional[str] = None
    repetir_senha: Optional[str] = field(
        default=None, metadata={"json_name": "repetirSenha"}
    )
