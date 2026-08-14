import pytest
from typing import List, Optional
from src.domain.entities.item import Item
from src.domain.interfaces.item_interface import ItemInterface
from src.use_cases.item_repo import ItemUOW


class FakeItemRepository(ItemInterface):
    def __init__(self):
        self.items: List[Item] = []
        self._counter = 1

    async def create(self, item: Item) -> Item:
        item.id = self._counter
        self._counter += 1
        self.items.append(item)
        return item

    async def get_by_id(self, item_id: int) -> Optional[Item]:
        return next((i for i in self.items if i.id == item_id), None)

    async def get_all(self) -> List[Item]:
        return self.items

    async def update(self, item: Item) -> Optional[Item]:
        for idx, i in enumerate(self.items):
            if i.id == item.id:
                self.items[idx] = item
                return item
        return None

    async def delete(self, item_id: int) -> bool:
        initial_len = len(self.items)
        self.items = [i for i in self.items if i.id != item_id]
        return len(self.items) < initial_len


@pytest.mark.anyio
async def test_create_item_use_case():
    repo = FakeItemRepository()
    use_case = ItemUOW(repo)
    created_item = await use_case.create(title="Test", description="Desc")

    assert created_item.id == 1
    assert created_item.title == "Test"