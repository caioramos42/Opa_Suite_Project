from enum import Enum
from dataclasses import dataclass

@dataclass
class Method:
    data: str
    action: str
    
class Actions(Enum):
    INSERT = Method('', 'POST')
    DELETE = Method('', 'DELETE')
    EDIT = Method('', 'PUT')
    EDIT_PARTIAL = Method('', 'PATCH')
    LIST = Method('listar', 'GET')