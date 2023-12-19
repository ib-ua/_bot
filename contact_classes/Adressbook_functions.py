from contact_classes import Phone, Address_book, Birthday, Email, Phone, Record, Name, Address

address_book_instance = Address_book.AddressBook()
record_instance = Record
phone_instance = Phone
birthday_instance = Birthday
name_instance = Name
email_instance = Email
address_instance = Address
# add_address_record = Record.Record.add_record()


def parse(user_input, commands):
    command = None
    for elem in commands:
        if user_input.startswith(elem):
            command = elem
            len_command = len(elem.split(' '))
            user_input_list = user_input.split(' ')
            args = user_input_list[len_command:]
            break
        if command is None:
            args = None
    return command, args


def input_error(func):

    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'The name is not in contacts. Enter a user name please.'
        except ValueError:
            return 'ValueError: Please enter a name followed by a phone.'
        except IndexError:
            return 'IndexError: Please enter a name followed by a phone.'
        except TypeError:
            return 'You have entered invalid number of arguments for this command.'
        except Phone.PhoneInvalidFormatError:
            return 'Invalid phone format. Please use one of format examples: +380951112233, 380951112233 or 0951112233'
        except Birthday.BirthdayInvalidFormatError:
            return 'Invalid birthday format. Please enter the birthday in the format YYYY-MM_DD'
        except Email.EmailInvalidFormatError:
            return 'Invalid email format.'

    return inner

@input_error
def add_contact(name, phone=None, birthday=None):
    if name in address_book_instance.data.keys():
        if phone is None:
            return f'A contact with named {name} already exists.'
        else:
            address_book_instance.data[name].add_phone(phone_instance.Phone(phone))
            if birthday is None:
                return f'Phone number {phone} has been assigned to contact named {name}.'
            else:
                address_book_instance.data[name].add_birthday(birthday_instance.Birthday(birthday))
                return f'Phone number {phone} and birthday {birthday} have been assigned to contact named {name}.'
    else:
        if phone is None:
            record = record_instance.Record(name_instance.Name(name))
            address_book_instance.add_record(record)
            return f'Contact named {name} has been added.'
        else:
            if birthday is None:
                record = record_instance.Record(name_instance.Name(name))
                record.add_phone(phone_instance.Phone(phone))
                address_book_instance.add_record(record)
                return f'Contact named {name} with a phone number {phone} has been added.'
            else:
                record = record_instance.Record(name_instance.Name(name), birthday_instance.Birthday(birthday))
                record.add_phone(phone_instance.Phone(phone))
                address_book_instance.add_record(record)
                return f"Contact named {name} with a phone number {phone} and {birthday} birthday has been added."


@input_error
def add_birthday(name, birthday):
    address_book_instance.data[name].add_birthday(birthday_instance.Birthday(birthday))
    return f"{name}'s birthday {birthday} has been added."


@input_error
def add_email(name, email):
    address_book_instance.data[name].add_email(email_instance.Email(email))
    return f"Email {email} for {name} has been added."


@input_error
def add_address(name, *address_args):
    address = ' '.join([*address_args])
    address_book_instance.data[name].add_address(address_instance.Address(address))
    return f"The address {address} for {name} has been added."  


@input_error
def change_contact(name, old_phone, new_phone):
    address_book_instance.data[name].remove_phone(Phone(old_phone))
    address_book_instance.data[name].add_phone(Phone(new_phone))
    return f"{name}'s phone number is now {new_phone}."


@input_error
def show_all(data=address_book_instance.data):
    phone_book = ''
    for name, info in data.items():
        phones = '--Phone numbers:\n'
        if data[name].phones:
            for phone in data[name].phones:
                phones += f'{phone.value}\n'
        else:
            phones += 'No phone numbers to display\n'
        phone_book += f'\n{name} ->\n{phones}'
        birthday = data[name].birthday
        if birthday is not None:
            phone_book += f'--birthday:\n{birthday.value}\n--days to birthday:\n{data[name].days_to_birthday()}\n'
        email = data[name].email
        if email is not None:
            phone_book += f'--Emails:\n{email.value}\n'
        address = data[name].address
        if address is not None:
            phone_book += f'--Address:\n{address.value}\n'
    return phone_book

def write_file():
    address_book_instance.save_data()

def greeting():
    return 'Hello! How can I help you?'


def end():
    return 'Good bye!'


def get_help():
    print("hello / hi".ljust(40), "to greet bot".rjust(80))
    print("Phone Book Commands".center(120, '-'))
    print("add <name> followed by a 12-digit <phone number> and <address>".ljust(80), "to add the data to your "
                                                                                       f"Book of Contacts".center(40))

    print("add birthday <name> <birthday, format YYYY-MM-DD>".ljust(80), "to add a birthday to a contact".rjust(40))
    print("add email <name> <email>".ljust(40), "to add the email to a specified contact".rjust(80))
    print("add address <name> <address>".ljust(40), "to add the address to a specified contact".rjust(80))
    print("change phone <name> <old phone> <new phone>".ljust(60), "to change the phone number of a "
                                                              "specified contact".rjust(60))

   
    print("show all".ljust(40), "to see all the contact details in your Book of Contacts".rjust(80))

    print("".center(120, "_"))

    print("General Commands".center(120, "-"))

    print("goodbye, close, or exit".ljust(40).rjust(80))
    print("".center(120, "_"))

    return ""