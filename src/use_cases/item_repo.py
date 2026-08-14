from typing import Protocol

from src.domain.interfaces.item_interface import ItemInterface
from src.domain.entities.item import Item


class ItemUOW(Protocol):
    def __init__(self, interface: ItemInterface):
        self.interface = interface

    async def get_by_id(self, id: int) -> Item:
        return await self.interface.get(value=id)

    async def create(self, item: Item) -> Item:
        return await self.interface.create(item)

    async def delete(self, id: int) -> None:
        return await self.interface.delete(id)
