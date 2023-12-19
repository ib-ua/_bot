from collections import UserDict
from contact_classes import Data_transfer

datatransfer_instance = Data_transfer



class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        filename = 'address_book.bin'
        data_loader = datatransfer_instance.DataTransfer(filename)
        loaded_data = data_loader.load_data()
        print(filename)
        if loaded_data:
            self.data = loaded_data

    def save_data(self):
        data_saver = datatransfer_instance.DataTransfer('address_book.bin')
        data_saver.save_data(self.data)

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
