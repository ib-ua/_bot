import re
from collections import UserDict
from ..models import AddressBook
from ..models import NoteBook


class InputProcessor(UserDict):
    def __init__(self, address_book: AddressBook, note_book: NoteBook):
        super().__init__()
        self.address_book = address_book
        self.note_book = note_book
        self.data['exit'] = lambda args: self.address_book.close()

    def process(self, user_input: str) -> str:
        [command, *args] = re.split(r'\s+', user_input.strip())
        return self.data.get(command, lambda x: "Command not found")(args)