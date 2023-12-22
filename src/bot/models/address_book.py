import re
from collections import UserDict
from typing import List

from .record import Record
from .data_transfer import DataTransferService


class AddressBook(UserDict[str, Record], DataTransferService):
    def __init__(self, name):
        super().__init__()
        self.filename = f'{name}_{self.__class__.__name__}.bin'
        data = self.load_data()

        if data:
            self.data.update(data)

    def add_record(self, record):
        self.data[record.name.value] = record

    def del_record(self, name):
        del self.data[name]

    def get_all_contacts(self) -> List[Record]:
        return list(self.data.values())

    def find_contacts_by_term(self, term: str) -> List[Record]:
        records = []
        for record in self.data.values():
            for field in [record.name, record.email, record.address, *record.phones]:
                if re.search(term, field, re.IGNORECASE):
                    records.append(record)
                    break
        return records

    def close(self):
        self.save_data(self.data)
