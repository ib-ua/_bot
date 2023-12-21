from .field import Field


class Content(Field):

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not value:
            raise ValueError("Empty value value")
        self.__value = value