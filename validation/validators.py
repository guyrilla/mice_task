from datetime import date, time
import re


def validate_name(name: str) -> str:
    if not re.match(r"[a-zA-Zа-яА-Я _]{2,}", name):
        raise ValueError(
            "Name must contain only letters, '_' and name length must be greater than 2"
        )

    return name


def validate_phone(phone: str) -> str:
    if not re.match(r"^(\+7|8)[0-9]{10,}$", phone):
        raise ValueError("Phone number must match +7XXXXXXXXX or 8XXXXXXXXXX")

    return phone


def validate_bookingdate(booking_date: date) -> date:
    booking_day = booking_date.day
    current_day: int = date.today().day
    day_offset = 90
    if not (booking_day >= current_day and booking_day <= (booking_day + day_offset)):
        raise ValueError(
            "Booking date must be greater or equal to the current day and must be no later than 90 days"
        )

    return booking_date


def validate_bookingtime(booking_time: time) -> time:
    booking_hour = booking_time.hour
    booking_minutes = booking_time.minute
    if not (12 <= booking_hour <= 22):
        raise ValueError(
            "Booking hour must be greater or equal to the 12 and less or equal to the 22"
        )

    if not (booking_minutes == 0):
        raise ValueError("Booking minutes must be equal to the 0")

    return booking_time


def validate_guests(number_of_guests: int) -> int:
    if not (type(number_of_guests) is int and number_of_guests in range(1, 12)):
        raise ValueError(
            "Number of guests must be an integer and be in the range from 1 to 12"
        )

    return number_of_guests
