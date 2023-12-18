import re
from collections import UserDict
from bot.models.AddressBook import AddressBook


class InputProcessor(UserDict):
    def __init__(self, address_book: AddressBook):
        super().__init__(address_book)

        self.address_book = address_book
        self.data['exit'] = lambda args: self.address_book.close()

    def process(self, user_input: str) -> str:
        [command, *args] = re.split(r'\s+', user_input.strip())
        return self.data.get(command, lambda x: "Command not found")(args)
