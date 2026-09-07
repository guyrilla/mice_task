import pytest
from datetime import date, time
from validation import validators


class TestValidateName:
    def test_valid_name(self):
        """Проверка валидного имени"""
        result = validators.validate_name("Иван Петров")
        assert result == "Иван Петров"

    def test_name_too_short(self):
        """Имя короче 2 символов"""
        with pytest.raises(
            ValueError,
            match="Name must contain only letters, '_', ' ' and name length must be greater than 2",
        ):
            validators.validate_name("A")

    def test_empty_name(self):
        """Пустое имя"""
        with pytest.raises(
            ValueError,
            match="Name must contain only letters, '_', ' ' and name length must be greater than 2",
        ):
            validators.validate_name("")


class TestValidatePhone:
    def test_valid_phone_plus7(self):
        """Валидный номер с +7"""
        result = validators.validate_phone("+79123456789")
        assert result == "+79123456789"

    def test_valid_phone_8(self):
        """Валидный номер с 8"""
        result = validators.validate_phone("89123456789")
        assert result == "89123456789"

    def test_invalid_phone_wrong_format(self):
        """Невалидный номер"""
        with pytest.raises(
            ValueError, match=r"Phone number must match \+7XXXXXXXXX or 8XXXXXXXXXX"
        ):
            validators.validate_phone("1234567890")


class TestValidateGuests:
    def test_valid_guests(self):
        """Валидное количество гостей"""
        result = validators.validate_guests(5)
        assert result == 5

    def test_guests_too_many(self):
        """Слишком много гостей"""
        with pytest.raises(
            ValueError,
            match="Number of guests must be an integer and be in the range from 1 to 12",
        ):
            validators.validate_guests(12)

    def test_guests_too_few(self):
        """Слишком мало гостей"""
        with pytest.raises(
            ValueError,
            match="Number of guests must be an integer and be in the range from 1 to 12",
        ):
            validators.validate_guests(0)


class TestValidateBookingTime:
    def test_valid_time(self):
        """Валидное время"""
        result = validators.validate_bookingtime(time(15, 0))
        assert result == time(15, 0)

    def test_time_too_early(self):
        """Слишком раннее время"""
        with pytest.raises(
            ValueError,
            match="Booking hour must be greater or equal to the 12 and less or equal to the 22",
        ):
            validators.validate_bookingtime(time(11, 0))

    def test_time_too_late(self):
        """Слишком позднее время"""
        with pytest.raises(
            ValueError,
            match="Booking hour must be greater or equal to the 12 and less or equal to the 22",
        ):
            validators.validate_bookingtime(time(23, 0))

    def test_time_not_on_hour(self):
        """Не ровный час"""
        with pytest.raises(ValueError, match="Booking minutes must be equal to the 0"):
            validators.validate_bookingtime(time(15, 30))
