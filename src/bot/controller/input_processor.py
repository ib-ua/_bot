import copy
import re
from collections import UserDict
from typing import List

from ..models import AddressBook
from ..models import NoteBook
from ..models.name import Name
from ..models.record import Record
from ..models.birthday import Birthday
from ..models.email import Email, EmailInvalidFormatError
from ..utils.sort import start

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except EmailInvalidFormatError:
            return 'Invalid email format.'
        except ValueError as e:
            error_message = 'Value error occurred.'
            if type(e.args[0]) is dict and 'message' in e.args[0]:
                error_message = e.args[0]['message']

            return error_message

    return inner


class InputProcessor(UserDict):
    def __init__(self, address_book: AddressBook, note_book: NoteBook):
        super().__init__()
        self.address_book = address_book
        self.note_book = note_book
        self.context = None

        self.data[None] = {
            'exit': lambda args: self.address_book.close(),
            'hello': lambda args: 'Hello',
            'add-contact': lambda args: self.create_contact(*args),
            'edit-contact': lambda args: self.edit_contact(*args),
            'sort-files' : lambda args: self.sort()
        }

        self.data[Record] = {
            'set-phones': lambda args: self.add_phone(*args),
            'set-birthday': lambda args: self.add_birthday(*args),
            'set-email': lambda args: self.add_email(*args),
            'add-address': lambda args: self.add_address(*args),
            'discard': lambda args: self.cancel_work_on_record(),
            'apply': lambda args: self.complete_work_on_record(),
            'exit': lambda args: self.address_book.close(),
        }

    def get_commands(self) -> List[str]:
        return list(self.data.get(type(self.context), self.data[None]).keys())

    def process(self, user_input: str) -> str:
        [command, *args] = re.split(r'\s+', user_input.strip())
        return self.data.get(type(self.context), self.data[None]).get(command, lambda x: "Command not found")(args)

    def create_contact(self, name: str):
        record = Record(Name(name))
        self.context = record
        return f'Creating "{record.name}"'
    
    def sort(self, *args):
        if not args:
            folder = input("Please enter the folder name: ")
            if not folder:
                raise IndexError
        else:
            folder = args[0]
        return start(folder)


    def add_phone(self, phone: str):
        record = self.context
        record.add_phone(phone)
        print(phone)

    def add_birthday(self, birthday_str: str):
        record = self.context
        birthday = Birthday(birthday_str)
        record.add_birthday(birthday)
        print(birthday)

    @input_error
    def add_email(self, email_str: str):
        email = Email(email_str)
        record = self.context
        record.add_email(email)
        return f'"{email}" added to contact "{record.name}"'

    def add_address(self, address: str):
        record = self.context
        record.add_address(address)
        print(address)

    def complete_work_on_record(self):
        self.address_book.add_record(self.context)
        self.context = None
        return 'Contact saved successfully'

    def cancel_work_on_record(self):
        self.context = None
        return 'Creating contact canceled'

    @input_error
    def edit_contact(self, contact_name: str):
        record = self.address_book.get(contact_name)
        if record is None:
            raise ValueError({'message': f'No contact with name "{contact_name}"'})
        self.context = copy.deepcopy(record)
