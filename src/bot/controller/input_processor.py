import re
from collections import UserDict
from typing import List


from ..models import AddressBook
from ..models import NoteBook
from ..models.record import Record
from ..models.email import Email, EmailInvalidFormatError



class InputProcessor(UserDict):
    def __init__(self, address_book: AddressBook, note_book: NoteBook):
        super().__init__()
        self.address_book = address_book
        self.note_book = note_book
        self.context = None

        self.data[None] = {
            'exit': lambda args: self.address_book.close(),
            'hello': lambda args: 'Hello',
            'add-contact': lambda args: self.create_contact(*args)
        }

        self.data[Record] = {
            'add-phones': lambda args: self.add_phone(*args),
            'add-birthday': lambda args: self.add_birthday(*args),
            'add-email': lambda args: self.add_email(*args),
            'add-address': lambda args: self.add_address(*args),
            'cancel': lambda args: self.cancel_work_on_record(),
            'ok': lambda args: self.complete_work_on_record()
        }

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except EmailInvalidFormatError:
                return 'Invalid email format.'
           

        return inner

    def get_input_message(self) -> List[str]:
        return list(self.data.get(type(self.context), self.data[None]).keys())

    def process(self, user_input: str) -> str:
        [command, *args] = re.split(r'\s+', user_input.strip())
        return self.data.get(type(self.context), self.data[None]).get(command, lambda x: "Command not found")(args)

    def create_contact(self, name: str):
        record = Record(name)
        self.context = record
        return f'Creating "{record.name}"' 

    def add_phone(self, phone: str):
        record = self.context
        record.add_phone(phone)
        print(phone)
    
    def add_birthday(self, birthday: str):
        record = self.context
        record.add_birthday(birthday)
        print(birthday)
    
    @input_error
    def add_email(self, email: str):
        email = Email(email)
        record = self.context
        record.add_email(email)
        print(dir(email))
        return f'"{email.value}" added to contact "{record.name}"' 

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
