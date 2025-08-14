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