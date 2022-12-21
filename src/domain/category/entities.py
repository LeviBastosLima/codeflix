from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from domain.common.validators import ValidatorRules
from src.domain.common.entities import EntityBase


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(EntityBase):
    name: str
    description: Optional[str] = field(default=None)
    is_active: Optional[bool] = field(default=True)
    created_at: datetime = field(default_factory=lambda: datetime.now())

    def __new__(cls, **kwargs):
        cls.validate(
            name=kwargs.get('name'),
            description=kwargs.get('description'),
            is_active=kwargs.get('is_active')
        )

        return super(Category, cls).__new__(cls)

    def update(self, name: str, description: str) -> None:
        self.validate(name, description)
        self._set('name', name)
        self._set('description', description)

    def activate(self):
        self._set('is_active', True)

    def deactivate(self) -> None:
        self._set('is_active', False)

    @classmethod
    def validate(cls, name: str, description: str, is_active: bool = None):
        ValidatorRules(name, 'name').required().string().max_length(max_length=255)
        ValidatorRules(description, 'description').string()
        ValidatorRules(is_active, 'is_active').boolean()
