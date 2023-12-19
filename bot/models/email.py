import re
from models import field



class Email(field):

        @field.value.setter
        def value(self, value):
            pattern = r"[A-Za-z][A-Za-z0-9._]+@[A-Za-z]+\.[A-Za-z]{2,}"
            if re.match(pattern, value) is not None:
                self._value = value
            else:
                raise EmailInvalidFormatError('Invalid email format')

class EmailInvalidFormatError(Exception):
    pass