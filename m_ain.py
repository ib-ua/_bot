from contact_classes import Adressbook_functions, Write_file

write_file_instance = Write_file
adressbook_instance = Adressbook_functions

def main():
    handler_commands = {'hello': adressbook_instance.greeting,
                        'hi': adressbook_instance.greeting,
                        'add birthday': adressbook_instance.add_birthday,
                        'add email': adressbook_instance.add_email,
                        'add address': adressbook_instance.add_address,
                        'change phone': adressbook_instance.change_contact,
                        'show all': adressbook_instance.show_all,
                        'add': adressbook_instance.add_contact,
                        'help': adressbook_instance.get_help,
                        'exit': adressbook_instance.end,
                        'good bye': adressbook_instance.end,
                        'close': adressbook_instance.end,
                        }
    print("Please enter your command or type 'help' to see the full list of available commands.")

    while True:
        user_input = input('Enter command or type "help": ')
        if user_input.lower() in handler_commands.keys():
            output = handler_commands[user_input.lower()]()
            print(output)
            if output == 'Good bye!':
                write_file_instance.write_file()
                exit()
        else:
            command, args = adressbook_instance.parse(user_input, handler_commands.keys())
            if command:
                
                print(handler_commands[command](*args))
            else:
                print("Unknown command. Please type 'help' to get the full list of available commands.")

if __name__ == '__main__':
    main()