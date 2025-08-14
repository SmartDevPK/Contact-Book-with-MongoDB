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