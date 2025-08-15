import sqlite3

# Database connection
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT
)''')

# Add new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                   (name, phone, email, address))
    conn.commit()
    print("Contact added successfully!\n")

# View all contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}, Address: {row[4]}")
    else:
        print("No contacts found.\n")

# Search contact
def search_contact():
    keyword = input("Enter name or phone to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}, Address: {row[4]}")
    else:
        print("No matching contacts found.\n")

# Update contact
def update_contact():
    contact_id = input("Enter contact ID to update: ")
    name = input("Enter new name: ")
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")
    address = input("Enter new address: ")

    cursor.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                   (name, phone, email, address, contact_id))
    conn.commit()
    print("Contact updated successfully!\n")

# Delete contact
def delete_contact():
    contact_id = input("Enter contact ID to delete: ")
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    print("Contact deleted successfully!\n")

# Main menu
while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")

conn.close()
