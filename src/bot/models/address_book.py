from collections import UserDict
from pathlib import Path


class AddressBook(UserDict):
    def __init__(self, name='data'):
        super().__init__()
        self.is_open = True
        self.name = name
        self.path = Path(name + '.bin')

    def close(self):
        self.is_open = False
        return "Buy!"

