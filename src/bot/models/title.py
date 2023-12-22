from .field import Field


class Title(Field):

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not value:
            raise ValueError("Empty value")
        self.__value = value
