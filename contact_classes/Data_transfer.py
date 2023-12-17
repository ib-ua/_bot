from pathlib import Path
from pickle import load, dump

class DataTransfer:

    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        if Path(self.filename).exists():
            with open(self.filename, 'rb') as file:
                return load(file)
        return None

    def save_data(self, data):
        with open(self.filename, 'wb') as file:
            dump(data, file)