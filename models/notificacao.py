from typing import Optional

from decorators.dataclass_to_dict import dataclass_to_dict


@dataclass_to_dict
class NotificacaoBody:
    type: str
    title: str
    description: str
    users: Optional[list[str]] = None
    link: Optional[str] = None
