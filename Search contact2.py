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
        results = []
        for contact in self.contacts:
            if (
                search_query.lower() in contact['first_name'].lower() or
                search_query.lower() in contact['last_name'].lower() or
                search_query.lower() in contact['phone_number'] or
                search_query.lower() in contact['email'].lower()
            ):
                results.append(contact)
        return results


# Приклад використання:

contact_book = ContactBook()

# Додавання контакту
contact_book.add_contact('Іван', 'Іванов', '123456789', 'ivan@example.com')
contact_book.add_contact('Петр', 'Петров', '987654321', 'petr@example.com')

# Поиск контактов
search_results = contact_book.search_contacts('Петр')
print("Результаты поиска:")
for result in search_results:
    print(result)
