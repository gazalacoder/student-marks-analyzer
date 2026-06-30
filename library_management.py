import tkinter as tk
from tkinter import messagebox

books = []

def update_counter():
    total_label.config(text=f"Total Books: {book_list.size()}")

def clear_fields():
    book_entry,delete(0, tk.END)
    author_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def add_book():
    book = book_entry.get()
    author = author_entry.get()
    quantity = quantity_entry.get()
    if book and author and quantity:
        data = f"Book: {book} | Author: {author} | Quantity: {quantity}"
        books.append(data)
        book_list.insert(tk.END, data)

        with open("library_books.tkt", "a") as file:
            file.write(data + "\n")
        update_counter()
        clear_fields()
        messagebox.showinfo("Success", "Book Added Successfully!")  
    else:
        messagebox.showerror("Error", "Please fill all fields!")  
       
def search_book():
    search = book_entry.get().lower()
    book_list.delete(0, tk.END)
    found = False
    for item in books:
        if search in item.lower():
            book_list.insert(tk.END, item)
            found = True
    if not found:
        messagebox.showerror("Not Found", "Book not found!")

def delete_book():
    selected = book_list.curselection()
    if selected:
        index = selected[0]
        book_list.delete(index)
        books.pop(index)
        update_counter()
        messagebox.showinfo("Deleted", "Book Deleted Successfully!")
    else:
        messagebox.showerror("Error", "Please select a book!")

def update_book():
    selected = book_list.curselection()
    if selected:
        index = selected[0]
        book = book_entry.get()
        author_entry.get()
        quantity_entry.get()
        if book and author and quantity:
            data = f"Book: {book} | Author: {author} | Quantity: {quantity}"
            books[index] = data
            book_list.delete(index)
            book_list.insert(index, data)
            clear_fields()
            messagebox.showinfo("Error", "Book Updated Successfully!")
    else:
        messagebox.showerror("Error", "Please select a book!")

def load_books():
    try:
        with open("library_books.txt", "r") as file:
            for line in file:
                data = line.strip()
                books.append(data)
                book_list.insert(tk.END, data)
        update_counter()
    except FileNotFoundError:
        pass                           

window = tk.Tk()
window.title("Library Management System")
window.geometry("700x550")
window.config(bg="#D6EAF8")

heading = tk.Label(window, text="Library Management System", font=("Arial", 20, "bold"), bg="#D6EAF8", fg="darkblue")
heading.pack(pady=15)

book_label = tk.Label(window, text="Book Name:", font=("Arial", 12, "bold"), bg="#D6EAF8")
book_label.pack()
book_entry = tk.Entry(window, width=30, font=("Arial", 12))
book_entry.pack(pady=5)

author_label = tk.Label(window, text="Author Name:", font=("Arial", 12, "bold"), bg="#D6EAF8")
author_label.pack()
author_entry = tk.Entry(window, width=30, font=("Arial", 12))
author_entry.pack(pady=5)

quantity_label = tk.Label(window, text="Quantity:", font=("Arial", 12, "bold"), bg="#D6EAF8")
quantity_label.pack()
quantity_entry = tk.Entry(window, width=30, font=("Arial", 12))
quantity_entry.pack(pady=5)

add_button = tk.Button(window, text="Add Book", font=("Arial", 12, "bold"), bg="green", fg="white", command=add_book)
add_button.pack(pady=10)

search_button = tk.Button(window, text="Search Book", font=("Arial", 12, "bold"), bg="blue", fg="white", command=search_book)
search_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Book", font=("Arial", 12, "bold"), bg="red", fg="white", command=delete_book)
delete_button.pack(pady=5)

update_button = tk.Button(window, text="Update Book", font=("Arial", 12, "bold"), bg="purple", fg="white", command=update_book)
update_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear Fields", font=("Arial", 12, "bold"), bg="orange", fg="white", command=clear_fields)
clear_button.pack(pady=5)

book_label = tk.Label(window, text="Available Books", font=("Arial", 12, "bold"), bg="#D6EAF8")
book_label.pack(pady=5)

book_list = tk.Listbox(window, width=75, height=10, font=("Arial", 11))
book_list.pack(pady=10)

total_label = tk.Label(window, text="Total Books: 0", font=("Arial", 12, "bold"), bg="#D6EAF8", fg="darkgreen")
total_label.pack(pady=5)
load_books()

window.mainloop()