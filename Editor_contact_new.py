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
            if any(search_query.lower() in value.lower() for value in contact.values()):
                results.append(contact)
        return results

    def edit_contact(self, search_query, updated_data):
        # Редагування контакту
        for contact in self.contacts:
            if any(search_query.lower() in value.lower() for value in contact.values()):
                # Оновлення даних контакту 
                contact.update(updated_data)
                return True  
        return False  

    def delete_contact(self, search_query):
        # Видалення контакту по запросу 
        for contact in self.contacts:
            if any(search_query.lower() in value.lower() for value in contact.values()):
                # Видалення контакту
                self.contacts.remove(contact)
                return True  
        return False  

# Создание экземпляра книги контактов
contact_book = ContactBook()

# Добавление контактов
contact_book.add_contact('Zahar', 'Krivenko', '123456789', 'zahar@example.com')
contact_book.add_contact('Alex', 'Gun', '987654321', 'alex@example.com')

# Редактирование контакта
edit_query = 'Zahar'
updated_data = {'phone_number': '555555555', 'email': 'new_email@example.com'}
if contact_book.edit_contact(edit_query, updated_data):
    print("Contact edited successfully")
else:
    print("Contact not found")

# Удаление контакта
delete_query = 'Петр'
if contact_book.delete_contact(delete_query):
    print("Contact deleted successfully")
else:
    print("Contact not found")
