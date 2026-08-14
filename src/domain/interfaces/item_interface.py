from typing import Protocol

from domain.entities.item import Item


class ItemInterface(Protocol):
    async def get(self, value) -> Item: ...

    async def create(self, item: Item) -> Item: ...

    async def delete(self, id: int) -> None: ...
