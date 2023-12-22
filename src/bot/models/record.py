from datetime import datetime
from typing import List

from .email import Email
from .birthday import Birthday
from .phone import Phone
from .address import Address
from .name import Name


class Record:
    def __init__(
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
        birthday = datetime.strptime(self.birthday.value, '%Y-%m-%d').date()
        today = datetime.now().date()
        birthday = birthday.replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        return (birthday - today).days

    def __repr__(self):

        # return f'{self.name}, {self.birthday}, {self.address}, [{", ".join([phone.value for phone in self.phones])}]'
        return '|{:^15}|{:^20}|{:^20}|{:^20}|{:^60}|'.format(
            str(self.name),
            str(self.email),
            str(self.birthday),
            str(self.address),
            ', '.join([str(phone) for phone in self.phones])
        )
