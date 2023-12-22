from .field import Field


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value.startswith('+') and len(value[1:]) == 12 and value[1:].isdigit() or value.isdigit() and len(value) in \
                (10, 12):
            self.__value = value
        else:
            raise PhoneInvalidFormatError('Invalid phone format. Please enter the phone in the format'
                                          ' +000000000000, 000000000000 or 0000000000')


class PhoneInvalidFormatError(Exception):
    pass
