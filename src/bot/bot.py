import atexit
import os

from rich.console import Console
from rich.table import Table

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from .controller.input_processor import InputProcessor
from .models.address_book import AddressBook
from .models.note_book import NoteBook


class Bot:
    def __init__(self, name=''):
        self.name = name
        self.lock = f'{name}_lock'
        open(self.lock, 'x').close()
        self.address_book = AddressBook(name)
        self.note_book = NoteBook(name)
        self.processor = InputProcessor(self.address_book, self.note_book)
        self.console = Console()
        atexit.register(self.stop)

    def start(self) -> None:
        while self.processor.is_running:
            commands = self.processor.get_commands()
            output = self.processor.process(
                prompt(f'Enter command:  {", ".join(commands)}\n', completer=WordCompleter(commands))
            )
            if type(output) is Table:
                self.console.print(output)
            else:
                print(output)
        self.stop()

    def stop(self) -> None:
        self.address_book.close()
        self.note_book.close()
        if os.path.isfile(self.lock):
            os.remove(self.lock)
