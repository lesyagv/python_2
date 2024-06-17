contacts = []

contact = {
    'first_name': 'john',
    'last_name': 'doe',
    'phone_number': '380111234567'
}

contacts.append(contact)

TITLE = "Your phone book"


def hello():
    print(F"Hi! Is's me, {TITLE.upper()}")


def bye():
    print(F"Thanks for using {TITLE}")


def make_your_choice():
    return input(f"Please make Your choice (l,a,u,r,h,c or q ) here>>> ") # додано очищення телефонної книги с


def help_me():
    print("""
    All that You can do:      
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        c : Clear
        q : Exit
    """)


def contact_list():
    if len(contacts) > 0:
        for contact in contacts:
            for k, v in contact.items():
                print(k, '=>', v)

    else:
        print("Your contact list is empty. Go back to menu yo add a new contact.")

def add_contact():
    contact = {}
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    phone_number = input("Enter phone number: ").strip()

    if not first_name or not last_name or not phone_number:
        print("One of the fields is empty. Try again.")
        return add_contact()
    if len(phone_number) != 12 or not phone_number.isdigit() or not phone_number.startswith("380"): # перевірка на прравильність номера
        print("Invalid phone number format. Please enter phone number in format 380xxxxxxxxx")
        return add_contact()

    for contact in contacts:
        if contact["first_name"] == first_name and contact["last_name"] == last_name or contact["phone_number"] == phone_number: # перевірка на дублі контактів
            print("A contact with the same name or phone number already exists.")
            print(f"{contact['first_name']} {contact['last_name']} {contact['phone_number']}")
            return add_contact()

    contact = {
               'first_name': first_name,
               'last_name': last_name,
               'phone_number': phone_number
    }

    return contact


def update_contact(contact):
    old_phone_number = contact['phone_number']
    old_first_name = contact['first_name']
    old_last_name = contact['last_name']

    phone_number = input(f"Edit phone number: ({old_phone_number}) => ").strip() or old_phone_number
    print(phone_number)
    first_name = input(f"Edit first name: ({old_first_name}) => ").strip() or old_first_name
    last_name = input(f"Edit last name: ({old_last_name}) => ").strip() or old_last_name

    return {'first_name': first_name.lower(), 'last_name': last_name.lower(), 'phone_number': phone_number}


def remove_contact(contact):
    index = contacts.index(contact)
    confirm = input("Are You sure You want to delete this  contact? (y/n): ").strip()
    if confirm.lower() in ('yes', 'y'):
        contacts.pop(index)

def clear_contact():
    index = contacts.index(contact)
    confirm = input("Are you sure you want to clear your phone book? (y/n): ").strip()
    if confirm.lower() in ('yes', 'y'):
        contacts.clear()


def lookup_contact(name):
    words = name.split()
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
        last_name = ''
    for d in contacts:
        if d['first_name'] == first_name.lower() and d['last_name'] == last_name.lower():
            return d
        elif d['first_name'] == first_name.lower() and last_name == '':
            return d


def main():
    hello()

    while True:
        match make_your_choice():
            case 'a':
                new_contact = add_contact()
                contacts.append(new_contact)
            case 'l':
                contact_list()

            case 'u':
                name = input("What name You looking for: ")
                contact = lookup_contact(name)
                contact.update(update_contact(contact))

            case 'r':
                name = input("What name You looking for: ")
                contact = lookup_contact(name)
                remove_contact(contact)

            case "c":
                clear_contact()

            case 'q':
                bye()
                break
            case _:
                help_me()


main()