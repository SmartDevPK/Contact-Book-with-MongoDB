from pymongo import MongoClient

client  = MongoClient("mongodb://localhost:27017/")
db = client['contact_book']
contacts = db ['contacts']


# FUNCTION FOR CRUD OPERATIONS

# Add a new contact
def add_contact(name, phone, emai):
    contact = {'name':name, 'phone':phone,  'email':emai}
    contacts.insert_one(contact)
    print(f"Name: {name}  added successfully")
    
# view all contacts
def view_contacts():
    for contact in contacts.find():
        print(f"Name:{contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(name):
    result = contacts.find_one({"name": name})
    if result:
        print(f"Name: {result['name']}, Phone:{result['phone']}, Email:{result['email']}")
    else:
        print(f"No contact found with name: {name}")
        
def delete_contact(name):
    result = contacts.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Contact with name: {name} deleted successfully")
    else:
        print(f"No contact found with name: {name}")
        
# Add simple menu for user interaction
while True:
    print("\nContact Book menu:")
    print("1. Add contact")
    print("2. view contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    
    choice = input("Enter Your Choice:")
    
    if choice == '1':
        name = input ("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
        
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Exiting the contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")