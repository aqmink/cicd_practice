from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ItemModel(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
