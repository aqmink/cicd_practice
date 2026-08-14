from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./app.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)

async_session = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)
