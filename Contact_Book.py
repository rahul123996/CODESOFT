import tkinter as tk
from tkinter import messagebox

# Create a dictionary to store contacts
contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_fields()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone number are required!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details["phone"]:
            contact_list.insert(tk.END, f"{name} - {details['phone']}")
            found = True
    if not found:
        messagebox.showinfo("No Results", "No contacts found!")

def update_contact():
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected).split(' - ')[0]
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name in contacts:
            contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
            clear_fields()
            update_contact_list()
        else:
            messagebox.showerror("Error", "Contact not found!")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected).split(' - ')[0]
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            update_contact_list()
        else:
            messagebox.showerror("Error", "Contact not found!")
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Contact Manager")

# Define the input fields and labels
name_label = tk.Label(window, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(window, text="Phone")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(window)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(window, text="Email")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=2, column=1)

address_label = tk.Label(window, text="Address")
address_label.grid(row=3, column=0)
address_entry = tk.Entry(window)
address_entry.grid(row=3, column=1)

# Buttons for actions
add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0)

update_button = tk.Button(window, text="Update Contact", command=update_contact)
update_button.grid(row=4, column=1)

delete_button = tk.Button(window, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=2)

# Search bar
search_label = tk.Label(window, text="Search")
search_label.grid(row=5, column=0)
search_entry = tk.Entry(window)
search_entry.grid(row=5, column=1)

search_button = tk.Button(window, text="Search", command=search_contact)
search_button.grid(row=5, column=2)

# Listbox to display contacts
contact_list = tk.Listbox(window, width=40, height=10)
contact_list.grid(row=6, column=0, columnspan=3)

# Initial display of contacts (empty)
update_contact_list()

# Run the application
window.mainloop()
