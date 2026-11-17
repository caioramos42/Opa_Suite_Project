from dataclasses import field
from typing import Optional

from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    id: Optional[str] = None
    id_fornecedor: Optional[str] = field(
        default=None, metadata={"json_name": "id_fornecedor"}
    )
    id_filial: Optional[str] = field(
        default=None, metadata={"json_name": "id_filial"}
    )
    nome: Optional[str] = None
    fantasia: Optional[str] = None
    cpf_cnpj: Optional[str] = field(default=None, metadata={"json_name": "cpf_cnpj"})
    status: Optional[str] = None
    prospect: Optional[bool] = None
    cliente: Optional[bool] = None
    fornecedor: Optional[bool] = None


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


@dataclass_to_dict
class ClienteBody:
    nome: str
    status: str
    prospect: bool
    cliente: bool
    fornecedor: bool
    prestador_servico: bool = field(metadata={"json_name": "prestadorServico"})
    cpf_cnpj: Optional[str] = field(
        default=None, metadata={"json_name": "cpf_cnpj"}
    )
    fantasia: Optional[str] = None
    tags: Optional[list[str]] = None
    id_fornecedor: Optional[str] = field(
        default=None, metadata={"json_name": "id_fornecedor"}
    )
    id_filial: Optional[str] = field(
        default=None, metadata={"json_name": "id_filial"}
    )


@dataclass_to_dict
class ClientePatchBody:
    nome: Optional[str] = None
    status: Optional[str] = None
    prospect: Optional[bool] = None
    cliente: Optional[bool] = None
    fornecedor: Optional[bool] = None
    prestador_servico: Optional[bool] = field(
        default=None, metadata={"json_name": "prestadorServico"}
    )
    cpf_cnpj: Optional[str] = field(
        default=None, metadata={"json_name": "cpf_cnpj"}
    )
    fantasia: Optional[str] = None
    tags: Optional[list[str]] = None
    id_fornecedor: Optional[str] = field(
        default=None, metadata={"json_name": "id_fornecedor"}
    )
    id_filial: Optional[str] = field(
        default=None, metadata={"json_name": "id_filial"}
    )

    def __post_init__(self) -> None:
        if all(getattr(self, name) is None for name in self.__dataclass_fields__):
            raise ValueError("Informe ao menos um campo para atualizar o cliente.")
