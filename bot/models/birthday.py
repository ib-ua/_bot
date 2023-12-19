from datetime import datetime
from bot.models.field import Field


class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        today = datetime.now().date()
        try:
            birthday = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            birthday = None
        if birthday is not None and birthday < today:
            self._value = value
        else:
            raise BirthdayInvalidFormatError('Invalid birthday format. Please enter the birthday'
                                             ' in the format YYYY-MM-DD')


class BirthdayInvalidFormatError(Exception):
    pass
