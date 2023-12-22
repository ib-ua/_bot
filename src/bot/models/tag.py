import re

from .field import Field


class Tag(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not value and re.search(r"\s+", value, re.IGNORECASE):
            raise ValueError("Empty value value")
        self.__value = value
