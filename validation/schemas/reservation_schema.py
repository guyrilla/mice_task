from pydantic import BaseModel, field_validator
from datetime import date, time
from validation import validators


class Reservation(BaseModel):
    name: str
    phone: str
    booking_date: date
    booking_time: time
    number_of_guests: int

    @field_validator("name")
    @classmethod
    def name_validator(cls, name: str):
        validators.validate_name(name)

    @field_validator("phone")
    @classmethod
    def phone_validator(cls, phone: str):
        validators.validate_phone(phone)

    @field_validator("booking_date")
    @classmethod
    def bookingdate_validator(cls, booking_date: date):
        validators.validate_bookingdate(booking_date)

    @field_validator("booking_time")
    @classmethod
    def bookingtime_validator(cls, booking_time: time):
        validators.validate_bookingtime(booking_time)

    @field_validator("number_of_guests")
    @classmethod
    def guests_validator(cls, number_of_guests: int):
        validators.validate_guests(number_of_guests)
