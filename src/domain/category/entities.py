from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass()
class Category:
    name: str
    description: Optional[str] = field(default=None)
    is_active: Optional[bool] = field(default=True)
    created_at: datetime = field(default_factory=lambda: datetime.now())
