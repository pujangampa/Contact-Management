import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)


def add_contact(contacts, name, phone):
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone}
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully.")


def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")


def search_contact(contacts, name):
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
    else:
        print("Contact not found.")


def list_contacts(contacts):
    if contacts:
        print("Contacts:")
        for name in contacts:
            print(name)
    else:
        print("No contacts found.")


def main_menu():
    contacts = load_contacts()
    while True:
        print("========================================")
        print("\tContact Management System")
        print("========================================\n")
        print("\t 1. Add Contact\n")
        print("\t 2. List Contact\n")
        print("\t 3. Search Contact\n")
        print("\t 4. Delete Contacts\n")
        print("\t 5. Exit\n")

        choice = input("\t Enter your choice (1-5): ")
        if choice == "1":
            name = input("\t Enter name: ")
            phone = input("\t Enter phone number: ")
            add_contact(contacts, name, phone)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            name = input("Enter name: ")
            search_contact(contacts, name)
        elif choice == "4":
            name = input("Enter name: ")
            delete_contact(contacts, name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
