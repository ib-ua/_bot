class ContactBook:
    def __init__(self):
        # Ініціюємо пусту книгу контактів
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number, email):
        # Додавання нового контакту 
        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)

    def search_contacts(self, search_query):
        # Пошук контакту
        results = []
        for contact in self.contacts:
            # Пошук через призвище ім'я номер телефону чи пошту
            if (
                search_query.lower() in contact['first_name'].lower() or
                search_query.lower() in contact['last_name'].lower() or
                search_query.lower() in contact['phone_number'] or
                search_query.lower() in contact['email'].lower()
            ):
                results.append(contact)
        return results

    def edit_contact(self, search_query, updated_data):
        # Редагування контакту
        for contact in self.contacts:
            if (
                search_query.lower() in contact['first_name'].lower() or
                search_query.lower() in contact['last_name'].lower() or
                search_query.lower() in contact['phone_number'] or
                search_query.lower() in contact['email'].lower()
            ):
                # Оновлення даних контакту 
                contact.update(updated_data)
                return True  
        return False  

    def delete_contact(self, search_query):
        # Видалення контакту по запросу 
        for contact in self.contacts:
            if (
                search_query.lower() in contact['first_name'].lower() or
                search_query.lower() in contact['last_name'].lower() or
                search_query.lower() in contact['phone_number'] or
                search_query.lower() in contact['email'].lower()
            ):
                # Видалення контакту
                self.contacts.remove(contact)
                return True  
        return False  
