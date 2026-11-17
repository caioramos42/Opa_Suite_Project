from dataclasses import field
from typing import Any, Optional

from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class OptionsList:
    skip: Optional[int] = None
    limit: Optional[int] = None


@dataclass_to_dict
class Filter:
    atalho: Optional[str] = None
    tipo_mensagem: Optional[str] = field(
        default=None, metadata={"json_name": "tipo_mensagem"}
    )


@dataclass_to_dict
class BodyList:
    filter: Optional[Filter] = None
    options: Optional[OptionsList] = None


@dataclass_to_dict
class EnvioTemplateBody:
    contato: dict[str, Any]
    template: dict[str, Any]
    canal: str
    allow_sending_to_started_customer_service: Optional[bool] = field(
        default=None,
        metadata={"json_name": "allowSendingToStartedCustomerService"},
    )
    open_customer_service: Optional[bool] = field(
        default=None, metadata={"json_name": "openCustomerService"}
    )
    metadata: Optional[dict[str, Any]] = None
