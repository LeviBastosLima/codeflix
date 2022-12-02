import json
import uuid
from abc import ABC
from dataclasses import dataclass, field, fields

from src.domain.common.exceptions import InvalidUuiException


@dataclass(frozen=True, slots=True)
class ValueObject(ABC):
    def __str__(self) -> str:
        fields_name = [field_object.name for field_object in fields(self)]
        first_attr = str(getattr(self, fields_name[0]))
        all_attrs = json.dumps(
            {field_name: getattr(self, field_name) for field_name in fields_name}
        )

        return first_attr if self.has_one_attr(fields_name) else all_attrs

    def has_one_attr(self, fields_name):
        return len(fields_name) == 1


@dataclass(frozen=True)
class UniqueEntityId(ValueObject):
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self) -> None:
        id_value = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self, 'id', id_value)
        self.__validate()

    def __validate(self) -> None:
        try:
            uuid.UUID(self.id)
        except ValueError as error:
            raise InvalidUuiException() from error
