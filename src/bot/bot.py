import atexit
import os

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from .controller.input_processor import InputProcessor
from .models.address_book import AddressBook
from .models.note_book import NoteBook


class Bot:
    def __init__(self, name=''):
        self.name = name
        open(f'{name}_lock', 'x').close()
        self.address_book = AddressBook(name)
        self.note_book = NoteBook(name)
        self.processor = InputProcessor(self.address_book, self.note_book)
        atexit.register(self.stop)

    def start(self) -> None:
        while self.processor.is_running:
            commands = self.processor.get_commands()
            print(
                self.processor.process(
                    prompt(f'Enter command:  {", ".join(commands)}\n', completer=WordCompleter(commands))
                )
            )
        self.stop()

    def stop(self) -> None:
        self.address_book.close()
        self.note_book.close()
        fn = f'{self.name}_lock'
        if os.path.isfile(fn):
            print('file')
            os.remove(fn)
