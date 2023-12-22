# BOT

## Project Description

The bot assistant uses a command pattern to parse user inputs and perform actions accordingly. It provides an easy and automated way to manage address book records (phones, birthday, etc.), keeping your contacts organized and accessible. Additionally, the bot allows you to make and manage notes, thus serving as a helpful tool for saving reminders, lists, or other important information. It features a robust architecture, allowing easy additions of new commands and functionalities.

## Project Usage Commands

The bot can be interacted with using certain commands from cli:

### Common Bot's Commands

- `hello`: Geet user in response.
- `exit`: Exit from the program.
- `sort-files <path>`: Sort files in selected directory by categories.

### Contacts Book Commands

- `add-contact/edit-contact <contact_name>`: Create/Edit contact.
  - `add-phone`: Add phone to contact's phone list.
  - `remove-phone`: Remove phone from contact's phone list. 
  - `set-birthday`: Set contact birthday.
  - `set-email`: Set contact email.
  - `set-address`: Set address for contact.
  - `apply`: Apply changes for contact.
  - `discard`: Discard changes for contact.
- `remove-contact <contact_name>`: Removes contact with provided name
- `get-contact-by-name <contact_name>`: Shows contact with provided name 
- `get-all-contacts`: Shows all contacts from address book
- `get-contacts-by-days-to-birthday <days>`: Show contact who has a birthday in specified days 
- `get-contacts-by-term <term>`: Shows contacts where any field has match with term 

### Notes Book Command

- `add-note/edit-note <note_title>`: Create/Edit note with name
  - `set-content`: Set content to note,
  - `add-tag`: Add tag to note,
  - `remove-tag`: Remove tag from note,
  - `apply`: Apply changes for note,
  - `discard`: Discard changes for note,
- `remove-note <note_title>`: Removes note with provided title
- `get-note-by-title <title>'`: Shows note with provided title
- `get-all-notes`: Shows all notes from Notes Books
- `get-notes-by-tag <tag>`: Shows all notes with provided tag
- `get-notes-by-term <term>`: Shows all notes where any field has match with term

## Setup & Requirements

The project uses Python 3.9.13 and has the following Python packages installed:

```py -m pip install -i https://test.pypi.org/simple/ t21_bot```

## Running the tests

The tests for the project are located in the `tests` module. You can run them using your preferred test runner.

## Contributions

Contributions to this project are welcome. Please feel free to open a pull request or branch.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors & Acknowledgment

Code authors, any acknowledgments, and anyone who has contributed to the development of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.