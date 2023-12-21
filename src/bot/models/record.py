from datetime import datetime,date
from typing import List

from .email import Email
from .birthday import Birthday
from .phone import Phone
from .address import Address
from .name import Name



class Record:
    def init(
            self, name: Name,
            phones: List[Phone] = None,
            birthday: Birthday = None,
            email: Email = None,
            address: Address = None
    ):
        self.name = name
        self.phones = [] if phones is None else phones
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
        if self.birthday is None:
            return None
        current_date: date = datetime.now().date()
        current_year: int = current_date.year
        current_year_birthday: date = self.birthday.value.replace(year=current_year)
        if current_year_birthday < current_date:
            current_year_birthday = current_year_birthday.replace(year=(current_year_birthday.year + 1))
        return (current_year_birthday - current_date).days