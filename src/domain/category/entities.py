from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from src.domain.common.entities import EntityBase


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(EntityBase):
    name: str
    description: Optional[str] = field(default=None)
    is_active: Optional[bool] = field(default=True)
    created_at: datetime = field(default_factory=lambda: datetime.now())

    def update(self, name: str, description: str) -> None:
        self._set('name', name)
        self._set('description', description)

    def activate(self):
        self._set('is_active', True)

    def deactivate(self) -> None:
        self._set('is_active', False)
