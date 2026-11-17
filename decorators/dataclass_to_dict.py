from dataclasses import dataclass, field, fields, is_dataclass
from typing import Any, TypeVar, dataclass_transform


T = TypeVar("T")


def _serialize(value: Any) -> Any:
    if is_dataclass(value) and not isinstance(value, type):
        return {
            field.metadata.get("json_name", field.name.replace("_", ".")): _serialize(field_value)
            for field in fields(value)
            if (field_value := getattr(value, field.name)) is not None
        }
    if isinstance(value, list):
        return [_serialize(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_serialize(item) for item in value)
    if isinstance(value, dict):
        return {key: _serialize(item) for key, item in value.items()}
    return value


@dataclass_transform(field_specifiers=(field,))
def dataclass_to_dict(cls: type[T]) -> type[T]:
    cls = dataclass(cls)

    def to_dict(self: Any) -> dict[str, Any]:
        return _serialize(self)

    setattr(cls, "to_dict", to_dict)
    return cls
