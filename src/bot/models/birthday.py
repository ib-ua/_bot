from datetime import datetime
from .field import Field


class Birthday(Field):
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        today = datetime.now().date()
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            birthday = None
        if birthday is not None and birthday < today:
            self.__value = value
        else:
            raise BirthdayInvalidFormatError('Invalid birthday format. Please enter the birthday'
                                             ' in the format YYYY-MM-DD')


class BirthdayInvalidFormatError(Exception):
    pass
