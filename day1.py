contacts = []

contacts = []  # This should be global or passed around

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print(f"Contact {name} added!")


def search_contact():
    name = input("Enter name to search: ")
    found_contacts = [c for c in contacts if c['name'].lower() == name.lower()]
    if found_contacts:  
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")                  
    else:
        print("No contacts found with that name.")      
    pass

def display_contacts():
    if contacts:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts available.") 
    pass

def delete_contact():
    name = input("Enter name to delete: ")
    global contacts 
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    print(f"Contact {name} deleted if it existed.") 
    pass

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")
    pass

if __name__ == "__main__":
    main()