from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from api.router import router as item_router
from infrastructure.db.conn import engine
from infrastructure.db.models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Асинхронное создание таблиц при старте
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Async Clean Architecture FastAPI CRUD", lifespan=lifespan)
app.include_router(item_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
