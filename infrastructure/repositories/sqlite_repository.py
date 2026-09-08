from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from domain import Reservation, IRepository
from infrastructure.models import ReservationModel


class SQLiteRepository(IRepository):
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_by_id(self, value: int) -> Reservation:
        stmt = select(ReservationModel).where(ReservationModel.id == value)
        result = await self.__session.execute(stmt)
        model = result.scalar_one_or_none()
        if model is None:
            raise ValueError(f"Reservation with id={value} not found")
        return self._to_entity(model)

    async def add_to_db(self, entity: Reservation) -> None:
        model: ReservationModel = self._to_model(entity)
        self.__session.add(model)
        await self.__session.commit()

    async def get_all(self) -> List[Reservation]:
        stmt = select(ReservationModel)
        result = await self.__session.execute(stmt)
        models = result.scalars().all()
        return [self._to_entity(model) for model in models]

    async def change_status(self, value: int) -> None:
        stmt = select(ReservationModel).where(ReservationModel.id == value)
        result = await self.__session.execute(stmt)
        model = result.scalar_one_or_none()
        if model is None:
            raise ValueError(f"Reservation with id={value} not found")
        model.status = "cancelled"
        await self.__session.commit()

    def _to_entity(self, model: ReservationModel) -> Reservation:
        return Reservation(
            id=model.id,
            name=model.name,
            phone=model.phone,
            booking_date=model.booking_date,
            booking_time=model.booking_time,
            number_of_guests=model.number_of_guests,
            status=model.status,
        )

    def _to_model(self, entity: Reservation) -> ReservationModel:
        return ReservationModel(
            id=entity.id,
            name=entity.name,
            phone=entity.phone,
            booking_date=entity.booking_date,
            booking_time=entity.booking_time,
            number_of_guests=entity.number_of_guests,
            status=entity.status,
        )
