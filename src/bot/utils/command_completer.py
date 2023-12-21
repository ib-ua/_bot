from prompt_toolkit.completion import WordCompleter


def command_completer():
    book_commands = [
    "add-contact",
    "add-birthday",
    "add-phones",
    "add-email",
    "add-address",

    "show-contacts",
    "phone",
    
    'cancel',
    'hello',
    'exit'
    ]
    notebook_commands = [
    
    ]
    commands = book_commands + notebook_commands
    return WordCompleter(commands)