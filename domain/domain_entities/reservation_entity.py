from validation import schemas


class Reservation(schemas.ReservationValidateSchema):
    id: int
    status: str
