from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    id: int | None
    title: str
    description: Optional[str] = None
