from collections import UserDict
from pathlib import Path
from .data_transfer import DataTransferService


class AddressBook(UserDict):
    def __init__(self, name='data'):
        super().__init__()
        self.name = name
        self.data_transfer_service = DataTransferService(Path(self.name + '.bin'))
        self.path = None
        self.is_open = True

    def save_data(self):
        self.data_transfer_service.save_data(self.data)

    def add_record(self, record):
        self.data[record.name.value] = record
        self.save_data()

    def del_record(self, name):
        del self.data[name]
        self.save_data()

    def iterator(self, n_records):
        page = {}
        i = 0
        for name, record in self.data.items():
            page[name] = record
            i += 1
            if i == n_records:
                yield page
                page = {}
                i = 0
        if page:
            yield page

    def close(self):
        self.is_open = False
        return "Bye!"
