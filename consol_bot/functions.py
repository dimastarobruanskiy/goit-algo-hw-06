from classes import Record


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."
    return inner

@input_error
def add_contact(args, book):
    name, phone = args

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.add_phone(phone)

    return "Contact added."

@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args

    record = book.find(name)

    if record is None:
        raise KeyError

    record.edit_phone(old_phone, new_phone)

    return "Contact updated."

@input_error
def show_phone(args, book):
    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    return str(record)

def show_all(book):
    if not book.data:
        return "No contacts found."

    result = ""
    for record in book.data.values():
        result += str(record) + "\n"

    return result.strip()

def delete_contact(args, book):
    name = args[0]
    book.delete(name)
    return "Deleted."