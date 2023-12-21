import re
from .field import Field


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        pattern = r"[A-Za-z][A-Za-z0-9._]+@[A-Za-z]+\.[A-Za-z]{2,}"
        if re.match(pattern, value) is not None:
            self.__value = value
        else:
            raise EmailInvalidFormatError('Invalid email format')


class EmailInvalidFormatError(Exception):
    pass
