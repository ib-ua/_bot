import copy
import re
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
from ..models.birthday import Birthday
from ..models.email import Email, EmailInvalidFormatError


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
            'add-note': lambda args: self.add_note(*args),
            'edit-note': lambda args: self.edit_note(*args),
            'get-all-notes': lambda args: self.get_all_notes(),
            'remove-note': lambda args: self.remove_note(*args),
            'get-note-by-title': lambda args: self.get_note_by_title(*args),
            'get-notes-by-tag': lambda args: self.get_notes_by_tag(*args),
            'get-notes-by-term': lambda args: self.get_notes_by_term(*args),
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

        self.data[Note] = {
            'set-content': lambda args: self.set_content(*args),
            'add-tag': lambda args: self.add_tag(*args),
            'remove-tag': lambda args: self.remove_tag(*args),
            'apply': lambda args: self.complete_work_on_note(),
            'discard': lambda args: self.cancel_work_on_note(),
            'exit': lambda args: self.address_book.close(),
        }

    def get_commands(self) -> List[str]:
        return list(self.data.get(type(self.context), self.data[None]).keys())

    def process(self, user_input: str) -> str:
        [command, *args] = re.split(r'\s+', user_input.strip(), 1)
        return self.data.get(type(self.context), self.data[None]).get(command, lambda x: "Command not found")(args)

    def create_contact(self, name: str):
        record = Record(Name(name))
        self.context = record
        return f'Creating "{record.name}"'

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
        self.note_book.add_note(self.context)
        self.context = None
        return 'Note saved successfully'
    
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
        return "\n".join([repr(note) for note in self.note_book.values()])
    
    def remove_note(self, value):
        note = self.note_book.find_note_by_title(value)
        self.note_book.delete_note(note)
        return 'Note was successfully deleted'
    
    def remove_tag(self, value):
        for tag in self.context.tags:
            if tag.value == value:
                self.context.delete_tag(tag)
                return f'Tag "{value}" was successfully deleted'
        return f'Failed to delete tag "{value}"'
        
    def get_note_by_title(self, title):
        return repr(self.note_book.find_note_by_title(title))
    
    def get_notes_by_tag(self, tag):
        return "\n".join([repr(note) for note in self.note_book.find_notes_by_tag(tag)])

    def get_notes_by_term(self, term):
        return "\n".join([repr(note) for note in self.note_book.find_note_by_term(term)])


    @input_error
    def edit_contact(self, contact_name: str):
        record = self.address_book.get(contact_name)
        if record is None:
            raise ValueError({'message': f'No contact with name "{contact_name}"'})
        self.context = copy.deepcopy(record)
