from .field import Field


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not value:
            raise ValueError({'message': 'Name cannot be empty'})
        self.__value = value
