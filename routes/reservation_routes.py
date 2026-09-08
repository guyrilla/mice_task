from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from domain.domain_entities.reservation_entity import Reservation, NewReservation
from domain.interfaces.db_repository import IRepository
from infrastructure import get_repository
from validation.schemas import ReservationValidateSchema

router = APIRouter()


@router.get("/bookings")
async def get_reserved_tables(
    db_repo: IRepository = Depends(get_repository),
) -> List[Reservation]:
    return await db_repo.get_all()


@router.post("/bookings", status_code=status.HTTP_201_CREATED)
async def add_reservation(
    data: ReservationValidateSchema,
    db_repo: IRepository = Depends(get_repository),
) -> Reservation:
    # проверка на пересечение по дате/времени — прямо тут, без отдельного репозиторного метода
    existing = await db_repo.get_all()
    for booking in existing:
        if (
            booking.booking_date == data.booking_date
            and booking.booking_time == data.booking_time
            and booking.status != "cancelled"
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Time slot already booked"
            )

    entity = NewReservation(**data.model_dump())
    return await db_repo.add_to_db(entity)


@router.get("/bookings/{id}")
async def get_reserved_table(
    id: int,
    db_repo: IRepository = Depends(get_repository),
) -> Reservation:
    reservation = await db_repo.get_by_id(id)
    if reservation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found"
        )
    return reservation


@router.delete("/bookings/{id}")
async def cancel_reservation(
    id: int,
    db_repo: IRepository = Depends(get_repository),
) -> Reservation:
    reservation = await db_repo.get_by_id(id)
    if reservation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found"
        )

    await db_repo.change_status(id, "cancelled")
    reservation.status = "cancelled"
    return reservation
