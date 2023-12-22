import copy
import re
from rich.table import Table
from colorama import Fore
from collections import UserDict
from typing import List
from ..models import AddressBook
from ..models import NoteBook
from ..models.note import Note
from ..models.title import Title
from ..models.content import Content
from ..models.tag import Tag
from ..models.name import Name
from ..models.record import Record
from ..models.email import Email, EmailInvalidFormatError
from ..models.phone import Phone, PhoneInvalidFormatError
from ..models.birthday import Birthday, BirthdayInvalidFormatError
from ..utils.sort import start


def input_error(func):
    def inner(*args, **kwargs):
        error_message = f'{Fore.RED}'
        try:
            result = func(*args, **kwargs)
            if type(result) is str:
                return f'{Fore.GREEN}{result}'
            else:
                return result

        except ValueError as e:
            if type(e.args[0]) is dict and 'message' in e.args[0]:
                error_message += e.args[0]['message']
            else:
                error_message += 'Value error occurred.'
        except EmailInvalidFormatError:
            error_message += 'Invalid email format.'
        except BirthdayInvalidFormatError:
            error_message += 'Invalid birthday format. Please enter the birthday in the format DD.MM.YYYY'
        except PhoneInvalidFormatError:
            error_message += 'Invalid phone format. Please use one of format examples: ' \
                             '+380951112233, 380951112233 or 0951112233'
        except TypeError:
            error_message += 'You have entered invalid number of arguments for this command.'
        return error_message

    return inner


def create_records_view(records: List[Record], title: str = 'Contacts'):
    table = Table(title=title)
    table.add_column("Name", justify="left", no_wrap=True, style="cyan")
    table.add_column("Address", justify="left")
    table.add_column("Birthday", justify="center", no_wrap=True)
    table.add_column("Email", justify="center", no_wrap=True)
    table.add_column("Phones", justify="center")

    for record in records:
        table.add_row(
            str(record.name),
            str(record.address) if record.address else "-",
            str(record.birthday) if record.birthday else "-",
            str(record.email) if record.email else "-",
            ", ".join([str(phone) for phone in record.phones]) if len(record.phones) else "-"
        )
    return table


def create_notes_view(notes: List[Note], title: str = 'Notes'):
    table = Table(title=title)
    table.add_column("Title", justify="center", no_wrap=True, style="cyan")
    table.add_column("Content", justify="left")
    table.add_column("Tags", justify="center")

    for note in notes:
        table.add_row(
            str(note.title),
            str(note.content) if note.content else "-",
            ", ".join([str(tag) for tag in note.tags]) if len(note.tags) else "-"
        )
    return table


class InputProcessor(UserDict):
    def __init__(self, address_book: AddressBook, note_book: NoteBook):
        super().__init__()
        self.is_running = True
        self.address_book = address_book
        self.note_book = note_book
        self.context = None

        self.data[None] = {
            'exit': lambda args: self.stop(),
            'hello': lambda args: 'Hello',
            'sort-files': lambda args: self.sort(),
            'add-contact': lambda args: self.create_contact(*args),
            'edit-contact': lambda args: self.edit_contact(*args),
            'get-all-contacts': lambda args: self.get_all_contacts(),
            'get-contacts-by-term': lambda args: self.get_contacts_by_term(*args),
            'get-contacts-by-days-to-birthday': lambda args: self.get_contacts_by_days_to_birthday(*args),
            'get-contact-by-name': lambda args: self.get_contact_by_name(*args),
            'add-note': lambda args: self.add_note(*args),
            'edit-note': lambda args: self.edit_note(*args),
            'get-all-notes': lambda args: self.get_all_notes(),
            'remove-note': lambda args: self.remove_note(*args),
            'get-note-by-title': lambda args: self.get_note_by_title(*args),
            'get-notes-by-tag': lambda args: self.get_notes_by_tag(*args),
            'get-notes-by-term': lambda args: self.get_notes_by_term(*args)
        }

        self.data[Record] = {
            'add-phone': lambda args: self.add_phone(*args),
            'set-birthday': lambda args: self.add_birthday(*args),
            'set-email': lambda args: self.add_email(*args),
            'add-address': lambda args: self.add_address(*args),
            'discard': lambda args: self.cancel_work_on_record(),
            'apply': lambda args: self.complete_work_on_record(),
            'exit': lambda args: self.stop(),
        }

        self.data[Note] = {
            'set-content': lambda args: self.set_content(*args),
            'add-tag': lambda args: self.add_tag(*args),
            'remove-tag': lambda args: self.remove_tag(*args),
            'apply': lambda args: self.complete_work_on_note(),
            'discard': lambda args: self.cancel_work_on_note(),
            'exit': lambda args: self.stop(),
        }

    def get_commands(self) -> List[str]:
        return list(self.data.get(type(self.context), self.data[None]).keys())

    def process(self, user_input: str) -> str:
        [command, *args] = re.split(r'\s+', user_input.strip(), 1)
        return self.data.get(type(self.context), self.data[None]).get(command, lambda x: "Command not found")(args)

    @input_error
    def create_contact(self, name: str) -> str:
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

    @input_error
    def add_phone(self, phone_str: str):
        phone = Phone(phone_str)
        record = self.context
        record.add_phone(phone)
        return f'Phone number "{phone}" added to contact "{record.name}"'

    @input_error
    def add_birthday(self, birthday_str: str):
        record = self.context
        birthday = Birthday(birthday_str)
        record.add_birthday(birthday)
        return f'Birthday date "{birthday}" added to contact "{record.name}"'

    @input_error
    def add_email(self, email_str: str):
        email = Email(email_str)
        record = self.context
        record.add_email(email)
        return f'E-mail "{email}" added to contact "{record.name}"'

    @input_error
    def add_address(self, address: str):
        record = self.context
        record.add_address(address)
        return f'Address "{address}" added to contact "{record.name}"'

    def get_all_contacts(self):
        return create_records_view(self.address_book.get_all_contacts(), 'All Contacts')

    def get_contacts_by_term(self, term):
        return create_records_view(self.address_book.find_contacts_by_term(term),
                                   f'All Contacts that\'s matches "{term}"')

    def complete_work_on_record(self):
        record = self.context
        self.address_book.add_record(record)
        self.context = None
        return create_records_view([record], f'Contact "{record.name}" saved successfully')

    def cancel_work_on_record(self):
        self.context = None
        return 'Creating contact canceled'

    def add_note(self, value):
        note = Note(Title(value))
        self.context = note
        return 'Creating note'

    def edit_note(self, title: str):
        note = self.note_book.get(title)
        if note is None:
            raise ValueError({'message': f'No note with title "{title}"'})
        self.context = copy.deepcopy(note)
        return f'Start editing note "{title}"'

    def complete_work_on_note(self):
        note = self.context
        self.note_book.add_note(note)
        self.context = None
        return create_notes_view([note], f'Note "{note.title}" saved successfully')

    def cancel_work_on_note(self):
        self.context = None
        return 'Creating note canceled'

    def set_content(self, value: str):
        content = Content(value)
        self.context.content = content
        return f'Content was added successfully to note "{self.context.title}"'

    def add_tag(self, value: str):
        tag = Tag(value)
        self.context.add_tag(tag)
        return f'Tag "{tag}" was added successfully to note "{self.context.title}"'

    def get_all_notes(self):
        return create_notes_view(list(self.note_book.values()), 'All Notes')

    def remove_note(self, value):
        note = self.note_book.find_note_by_title(value)
        self.note_book.delete_note(note)
        return f'Note {value} was successfully deleted'

    def remove_tag(self, value):
        for tag in self.context.tags:
            if tag.value == value:
                self.context.delete_tag(tag)
                return f'Tag "{value}" was successfully deleted'
        return f'Failed to delete tag "{value}"'

    def remove_phone(self, value):
        for phone in self.context.phones:
            if phone.value == value:
                self.context.remove_phone(phone)
                return f'Phone "{value}" was successfully deleted'
        return f'Failed to delete phone "{value}"'

    def get_note_by_title(self, title):
        return create_notes_view([self.note_book.find_note_by_title(title)], f'Note "{title}"')

    def get_notes_by_tag(self, tag):
        return create_notes_view(self.note_book.find_notes_by_tag(tag), f'All Notest that\'s has tag "{tag}"')

    def get_notes_by_term(self, term):
        return create_notes_view(self.note_book.find_note_by_term(term), f'All Notest that\'s matches "{term}"')

    @input_error
    def edit_contact(self, contact_name: str):
        record = self.address_book.get(contact_name)
        if record is None:
            raise ValueError({'message': f'No contact with name "{contact_name}"'})
        self.context = copy.deepcopy(record)

    def stop(self):
        self.is_running = False
        return 'Good bye!'

    @input_error
    def get_contact_by_name(self, name):
        return create_records_view([self.address_book.find_contact_by_name(name)], 'Contact for "name')

    @input_error
    def get_contacts_by_days_to_birthday(self, days_to_birthday_str: str):
        contacts = self.address_book.get_all_contacts()
        days_to_birthday = int(days_to_birthday_str)
        return create_records_view(
            [record for record in contacts if record.days_to_birthday() == days_to_birthday],
            f'Contacts that have birthday in {days_to_birthday_str}'
        )
