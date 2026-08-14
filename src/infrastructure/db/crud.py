from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.item import Item
from src.domain.interfaces.item_interface import ItemInterface
from src.infrastructure.db.models import ItemModel


class SQLAlchemyItemRepo(ItemInterface):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, item: Item) -> Item:
        db_item = ItemModel(title=item.title, description=item.description)
        self.db.add(db_item)
        await self.db.commit()
        await self.db.refresh(db_item)
        return Item(id=db_item.id, title=db_item.title, description=db_item.description)

    async def get_by_id(self, item_id: int) -> Optional[Item]:
        result = await self.db.execute(select(ItemModel).where(ItemModel.id == item_id))
        db_item = result.scalar_one_or_none()
        if db_item:
            return Item(id=db_item.id, title=db_item.title, description=db_item.description)
        return None

    async def delete(self, item_id: int) -> bool:
        result = await self.db.execute(select(ItemModel).where(ItemModel.id == item_id))
        db_item = result.scalar_one_or_none()
        if not db_item:
            return False
        await self.db.delete(db_item)
        await self.db.commit()
        return True