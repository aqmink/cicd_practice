from typing import Protocol

from domain.interfaces.item_interface import ItemInterface
from domain.entities.item import Item


class ItemUOW(Protocol):
    def __init__(self, interface: ItemInterface):
        self.interface = interface

    async def get_by_id(self, id: int) -> Item:
        return await self.interface.get(id=id)

    async def create(self, item: Item) -> Item:
        return await self.interface.create(item)

    async def delete(self, id: int) -> None:
        return await self.interface.delete(id)
