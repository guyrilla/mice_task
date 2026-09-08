from abc import ABC, abstractmethod
from typing import Optional, List
from domain import Reservation
from infrastructure import ReservationModel


class IRepository(ABC):
    @abstractmethod
    async def get_by_id(self, value: int) -> Optional[Reservation]:
        pass

    @abstractmethod
    async def add_to_db(self, entity: Reservation) -> None:
        pass

    @abstractmethod
    async def get_all(self) -> List[Reservation]:
        pass

    @abstractmethod
    async def change_status(self, value: int) -> None:
        pass

    @abstractmethod
    def _to_entity(self, model: ReservationModel) -> Reservation:
        pass

    @abstractmethod
    def _to_model(self, entity: Reservation) -> ReservationModel:
        pass
