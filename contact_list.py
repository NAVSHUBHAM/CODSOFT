class contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

def show_menu():
    print("Contact book 1.0 Menu :")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Quit")

def add_contact(contact_list):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact = contact(name, phone, email)
    contact_list.append(contact)
    print("Contact added successfully!")

def view_contacts(contact_list):
    if not contact_list:
        print("Not available!!")
        return

    print("Contacts:")
    for contact in contact_list:
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def search_contact(contact_list):
    if not contact_list:
        print("No contacts available.")
        return

    search_name = input("Enter the name to search: ")
    found_contacts = [contact for contact in contact_list if search_name.lower() in contact.name.lower()]

    if found_contacts:
        print("Matching Contacts:")
        for contact in found_contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
    else:
        print("No matching contacts found.")

def main():
    contact_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact(contact_list)
        elif choice == "2":
            view_contacts(contact_list)
        elif choice == "3":
            search_contact(contact_list)
        elif choice == "4":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
