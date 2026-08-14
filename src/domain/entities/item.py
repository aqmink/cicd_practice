from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    id: int | None = None
    title: str
    description: Optional[str] = None
