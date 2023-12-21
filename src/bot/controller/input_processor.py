import copy
import re
from colorama import Fore
from colorama import Fore
from collections import UserDict
from typing import List
from ..models import AddressBook
from ..models import NoteBook
from ..models.name import Name
from ..models.record import Record
from ..models.birthday import Birthday
from ..models.email import Email, EmailInvalidFormatError
from ..models.phone import Phone, PhoneInvalidFormatError
from ..models.birthday import Birthday, BirthdayInvalidFormatError

from ..models.phone import Phone, PhoneInvalidFormatError
from ..models.birthday import Birthday, BirthdayInvalidFormatError


default = 'default'
record_create = 'record_create'
record_edit = 'record_edit'


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except EmailInvalidFormatError:
            return Fore.RED + 'Invalid email format.'
        except ValueError as e:
            error_message = 'Value error occurred.'
            if type(e.args[0]) is dict and 'message' in e.args[0]:
                error_message = e.args[0]['message']

            return error_message
        except BirthdayInvalidFormatError:
            return Fore.RED + 'Invalid birthday format. Please enter the birthday in the format DD.MM.YYYY'
        except PhoneInvalidFormatError:
            return Fore.RED + 'Invalid phone format. Please use one of format examples: +380951112233, 380951112233 or 0951112233'
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
            'edit-contact': lambda args: self.edit_contact(*args)
,
            'show-contacts': lambda args: self.get_all_contacts(*args)
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
        return Fore.GREEN + f'Creating "{record.name}"'

    @input_error
    def add_phone(self, phone_str: str):
        phone = Phone(phone_str)
        record = self.context
        record.add_phone(phone)
        return Fore.GREEN + f'Phone number "{phone}" added to contact "{record.name}"'
        return Fore.GREEN + f'Phone number "{phone}" added to contact "{record.name}"'

    @input_error
    @input_error
    def add_birthday(self, birthday_str: str):
        record = self.context
        birthday = Birthday(birthday_str)
        record = self.context_value
        record = self.context_value
        record.add_birthday(birthday)
        return Fore.GREEN + f'Birthday date "{birthday}" added to contact "{record.name}"'
        return Fore.GREEN + f'Birthday date "{birthday}" added to contact "{record.name}"'

    @input_error
    def add_email(self, email_str: str):
        email = Email(email_str)
        record = self.context
        record.add_email(email)
        return Fore.GREEN + f'E-mail "{email}" added to contact "{record.name}"'
    
    @input_error
        return Fore.GREEN + f'E-mail "{email}" added to contact "{record.name}"'
    
    @input_error
    def add_address(self, address: str):
        record = self.context
        record.add_address(address)
        return Fore.GREEN + f'Address "{address}" added to contact "{record.name}"'

    def get_all_contacts(self):
        records = self.address_book.values()
        record = [record for record in records]
        print(f'RECORD{record}')
        for i in record:
            print(i)
        
        # phone_book = AddressBook(name='data')
        # print(phone_book)
        # for name, info in data.items():
        #     phones = '--Phone numbers:\n'
        #     if data[name].phones:
        #         for phone in data[name].phones:
        #             phones += f'{phone.value}\n'
        # else:
        #     phones += 'No phone numbers to display\n'
        # phone_book += f'\n{name} ->\n{phones}'
       
        return
        return Fore.GREEN + f'Address "{address}" added to contact "{record.name}"'

    def get_all_contacts(self):
        records = self.address_book.values()
        record = [record for record in records]
        print(f'RECORD{record}')
        for i in record:
            print(i)
        
        # phone_book = AddressBook(name='data')
        # print(phone_book)
        # for name, info in data.items():
        #     phones = '--Phone numbers:\n'
        #     if data[name].phones:
        #         for phone in data[name].phones:
        #             phones += f'{phone.value}\n'
        # else:
        #     phones += 'No phone numbers to display\n'
        # phone_book += f'\n{name} ->\n{phones}'
       
        return

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
