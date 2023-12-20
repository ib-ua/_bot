from .controller.input_processor import InputProcessor
from .models.address_book import AddressBook
from .models.note_book import NoteBook

class Bot:
    def __init__(self,  address_book_name):
        self.address_book = AddressBook(address_book_name)
        self.note_book = NoteBook()
        self.processor = InputProcessor(self.address_book, self.note_book)

    def start(self) -> None:
        while self.address_book.is_open:
            print(
                self.processor.process(
                    input(f'Enter command:  { ", ".join(self.processor.get_input_message()) }\n')
                )
            )
