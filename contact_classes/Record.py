import datetime


class Record:
    def __init__(self, name, birthday=None, email=None, address=None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        self.email = email
        self.address = address

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, rem_phone):
        for phone in self.phones:
            if phone.value == rem_phone.value:
                self.phones.remove(phone)

    def add_birthday(self, birthday):
        self.birthday = birthday

    def add_email(self, email):
        self.email = email

    def add_address(self, address):
        self.address = address

    def days_to_birthday(self):
        birthday = datetime.strptime(self.birthday.value, '%Y-%m-%d').date()
        today = datetime.now().date()
        birthday = birthday.replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        return (birthday - today).days