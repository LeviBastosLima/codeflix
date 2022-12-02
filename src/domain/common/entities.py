from abc import ABC
from dataclasses import dataclass, field, asdict

from src.domain.common.value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class EntityBase(ABC):
    unique_entity_id: UniqueEntityId = field(
        default_factory=lambda: UniqueEntityId(), init=False
    )

    @property
    def id(self):
        return str(self.unique_entity_id)

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop('unique_entity_id')
        entity_dict['id'] = self.id
        return entity_dict
