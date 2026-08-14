from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.conn import async_session
from src.infrastructure.db.crud import SQLAlchemyItemRepo
from src.use_cases.item_repo import ItemUOW


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


def get_item_repo(db: AsyncSession = Depends(get_db)) -> ItemUOW:
    return SQLAlchemyItemRepo(db)


def get_item_use_cases(
    repo: SQLAlchemyItemRepo = Depends(get_item_repo)
) -> ItemUOW:
    return ItemUOW(repo)
