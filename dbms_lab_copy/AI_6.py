import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Function to connect to the MySQL database
def connect_to_database():
    global db
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root@localhost',
            password='root',
            database='chat_gpt'
        )
        messagebox.showinfo("Success", "Connected to the database")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to insert data into the database
def insert_data():
    cursor = db.cursor()
    name = entry_name.get()
    try:
        cursor.execute("INSERT INTO my_table (name) VALUES (%s)", (name,))
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
    except mysql.connector.Error as err:
        db.rollback()
        messagebox.showerror("Error", f"Error: {err}")
    cursor.close()

# Create a basic tkinter window
root = tk.Tk()
root.title("Database Operations")

# Connect to the database button
connect_button = tk.Button(root, text="Connect to Database", command=connect_to_database)
connect_button.pack()

# Data Entry
label_name = tk.Label(root, text="Name:")
entry_name = tk.Entry(root)
label_name.pack()
entry_name.pack()

# Insert Data button
insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.pack()

# Main loop for the tkinter window
root.mainloop()
