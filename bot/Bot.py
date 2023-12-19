from bot.controller.InputProcessor import InputProcessor
from models import AddressBook


class Bot:
    def __init__(self,  address_book_name):
        self.address_book = AddressBook(address_book_name)
        self.processor = InputProcessor(self.address_book)

    def start(self) -> None:
        while self.address_book.is_open:
            print(
                self.processor.process(
                    input("What would you like to do?\n")
                )
            )
