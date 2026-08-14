from typing import Optional
from pydantic import BaseModel


class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None


class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        from_attributes = True
