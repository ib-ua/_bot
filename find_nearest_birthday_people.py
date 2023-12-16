from datetime import datetime, date, timedelta # Import datetime-related modules.

def find_nearest_birthday_people(self, number_of_days):
    # Method to find contacts with birthdays within a specified number of days.
    today = datetime.today().date()
    today_future_date = today + timedelta(days=number_of_days)
    contacts_within_timeframe = []

    for contact in self.data:
        split_char = contact.birthday[2]
        birthday_of_contact = contact.birthday.split(split_char)
        birthday_of_contact = date(int(birthday_of_contact[2]), int(birthday_of_contact[1]), int(birthday_of_contact[0]))
        birthday_of_contact = birthday_of_contact.replace(year=today.year)
        if today <= birthday_of_contact <= today_future_date:
            contacts_within_timeframe.append(contact)