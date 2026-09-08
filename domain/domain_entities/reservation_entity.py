from validation import schemas


class NewReservation(schemas.ReservationValidateSchema):
    pass


class Reservation(schemas.ReservationValidateSchema):
    id: int
    status: str
