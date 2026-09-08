# core/app.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import router
from infrastructure.database import init_models


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield


entry = FastAPI(lifespan=lifespan)
entry.include_router(router)
