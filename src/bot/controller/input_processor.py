import re
from collections import UserDict
from typing import List

from ..models import AddressBook
from ..models import NoteBook
from ..models.name import Name
from ..models.record import Record
from ..models.birthday import Birthday
from ..models.email import Email, EmailInvalidFormatError

default = 'default'
record_create = 'record_create'
record_edit = 'record_edit'


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except EmailInvalidFormatError:
            return 'Invalid email format.'

    return inner


class InputProcessor(UserDict):
    def __init__(self, address_book: AddressBook, note_book: NoteBook):
        super().__init__()
        self.address_book = address_book
        self.note_book = note_book
        self.context: str = default
        self.context_value = None

        self.data[default] = {
            'exit': lambda args: self.address_book.close(),
            'hello': lambda args: 'Hello',
            'add-contact': lambda args: self.create_contact(*args)
        }

        self.data[record_create] = {
            'add-phones': lambda args: self.add_phone(*args),
            'add-birthday': lambda args: self.add_birthday(*args),
            'add-email': lambda args: self.add_email(*args),
            'add-address': lambda args: self.add_address(*args),
            'cancel': lambda args: self.cancel_work_on_record(),
            'ok': lambda args: self.complete_work_on_record()
        }

    def get_commands(self) -> List[str]:
        return list(self.data.get(self.context, self.data[default]).keys())

    def process(self, user_input: str) -> str:
        [command, *args] = re.split(r'\s+', user_input.strip())
        return self.data.get(self.context, self.data[default]).get(command, lambda x: "Command not found")(args)

    def create_contact(self, name: str):
        record = Record(Name(name))
        self.context = record_create
        self.context_value = record
        return f'Creating "{record.name}"'

    def add_phone(self, phone: str):
        record = self.context_value
        record.add_phone(phone)
        print(phone)

    def add_birthday(self, birthday_str: str):
        record = self.context_value
        birthday = Birthday(birthday_str)
        record.add_birthday(birthday)
        print(birthday)

    @input_error
    def add_email(self, email_str: str):
        email = Email(email_str)
        record = self.context_value
        record.add_email(email)
        return f'"{email}" added to contact "{record.name}"'

    def add_address(self, address: str):
        record = self.context_value
        record.add_address(address)
        print(address)

    def complete_work_on_record(self):
        self.address_book.add_record(self.context_value)
        self.context_value = None
        self.context = default
        return 'Contact saved successfully'

    def cancel_work_on_record(self):
        self.context_value = None
        self.context = default
        return 'Creating contact canceled'
