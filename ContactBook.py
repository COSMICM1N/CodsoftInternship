class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone_number']}")

    def search_contact(self, keyword):
        results = []
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone_number']:
                results.append((name, details))
        if not results:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for name, details in results:
                print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone_number, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter search keyword: ")
            manager.search_contact(keyword)
        elif choice == '4':
            name = input("Enter contact name to update: ")
            phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, phone_number, email, address)
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()