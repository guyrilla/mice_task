from infrastructure.database import Base
from sqlalchemy import String, Integer, Date, Time
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, time


class ReservationModel(Base):
    __tablename__ = "reservation"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    booking_date: Mapped[date] = mapped_column(Date, nullable=False)
    booking_time: Mapped[time] = mapped_column(Time, nullable=False)
    number_of_guests: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
