from abc import ABC, abstractmethod
from typing import List, Optional
from domain.domain_entities.reservation_entity import Reservation, NewReservation


class IRepository(ABC):
    @abstractmethod
    async def get_by_id(self, value: int) -> Optional[Reservation]: ...

    @abstractmethod
    async def add_to_db(self, entity: NewReservation) -> Reservation: ...

    @abstractmethod
    async def get_all(self) -> List[Reservation]: ...

    @abstractmethod
    async def change_status(self, value: int, new_status: str) -> None: ...
