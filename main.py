from contact_classes import Adressbook_functions, Write_file

def main():
    handler_commands = {'hello': Adressbook_functions.greeting,
                        'hi': Adressbook_functions.greeting,
                        'add birthday': Adressbook_functions.add_birthday,
                        'add email': Adressbook_functions.add_email,
                        'add address': Adressbook_functions.add_address,
                        'change phone': Adressbook_functions.change_contact,
                        'show all': Adressbook_functions.show_all,
                        'add': Adressbook_functions.add_contact,
                        'help': Adressbook_functions.get_help,
                        'exit': Adressbook_functions.end,
                        'good bye': Adressbook_functions.end,
                        'close': Adressbook_functions.end,
                        }

    print("Please enter your command or type 'help' to see the full list of available commands.")

    while True:
        user_input = input('Enter command or type "help": ')
        if user_input.lower() in handler_commands.keys():
            output = handler_commands[user_input.lower()]()
            print(output)
            if output == 'Good bye!':
                Write_file.write_file()
                exit()
        else:
            command, args = Adressbook_functions.parse(user_input, handler_commands.keys())
            if command:
                print(handler_commands[command](*args))
            else:
                print("Unknown command. Please type 'help' to get the full list of available commands.")


if __name__ == '__main__':
    main()