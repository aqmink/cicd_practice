from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    title: str
    description: Optional[str] = None
    id: int | None = None
