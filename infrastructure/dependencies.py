from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database import get_session
from infrastructure.repositories.sqlite_repository import SQLiteRepository
from domain import IRepository


def get_repository(session: AsyncSession = Depends(get_session)) -> IRepository:
    return SQLiteRepository(session)
