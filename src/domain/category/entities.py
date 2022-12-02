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
