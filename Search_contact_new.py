class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number, email):
        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)

    def search_contacts(self, search_query):
        results = [contact for contact in self.contacts if any(search_query.lower() in value.lower() for value in contact.values())]
        return results


# Приклад використання:

contact_book = ContactBook()

# Додавання контакту
contact_book.add_contact('Zahar', 'Krivenko', '0502146269', 'zakhar@example.com')
contact_book.add_contact('Петр', 'Петров', '987654321', 'petr@example.com')

# Поиск контактов
search_results = contact_book.search_contacts('Zahar')
print("Determination results:")
for result in search_results:
    print(result)
