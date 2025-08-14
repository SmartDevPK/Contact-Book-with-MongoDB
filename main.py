from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

# -----------------------------
# Connect to MongoDB
# -----------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client['contact_book']
contacts = db['contacts']

# -----------------------------
# Flask App Setup
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Routes
# -----------------------------

# Home page - list all contacts
@app.route('/')
def index():
    all_contacts = list(contacts.find())
    return render_template('index.html', contacts=all_contacts)

# Add new contact
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    contacts.insert_one({'name': name, 'phone': phone, 'email': email})
    return redirect('/')

# Search contact
@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    result = contacts.find_one({'name': name})
    return render_template('search.html', contact=result, name=name)

# Delete contact
@app.route('/delete/<name>')
def delete(name):
    contacts.delete_one({'name': name})
    return redirect('/')

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
