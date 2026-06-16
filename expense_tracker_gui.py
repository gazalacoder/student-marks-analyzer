import tkinter as tk

window = tk.Tk()
window.title("Expense Tracker")
window.geometry("450x600")
window.config(bg="#87CEEB")

heading = tk.Label(window, text="Expense Tracker", font=("Arial", 22, "bold"), bg="#87CEEB", fg="darkblue")
heading.pack(pady=20)

name_label = tk.Label(window, text="Expense Tracker", font=("Arial", 14), bg="#87CEEB")
name_label.pack()
name_entry = tk.Entry(window, font=("Arial", 14), width=25)
name_entry.pack(pady=5)

amount_label = tk.Label(window, text="Amount", font=("Arial", 14), bg="#87CEEB")
amount_label.pack()
amount_entry = tk.Entry(window, font=("Arial", 14), width=25)
amount_entry.pack(pady=5)

category_label = tk.Label(window, text="Category", font=("Arial", 14), bg="#87CEEB")
category_label.pack()

category_var = tk.StringVar()
category_var.set("Food")
category_menu = tk.OptionMenu(window, category_var, "Food", "Travel", "Shopping", "Bills")
category_menu.config(font=("Arial", 12), width=15)
category_menu.pack(pady=10)

expenses = []

def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()
    category = category_var.get()

    if name and amount:
        expense = f"{category} - {name} - ₹{amount}"
        expense_list.insert(tk.END, expense)
        expenses.append(int(amount))
        total_label.config(text=f"Total Expense: ₹{sum(expenses)}")
        name_entry,delete(0, tk.END)
        amount_entry,delete(0, tk.END)

def clear_all():
    expense_list.delete(0, tk.END)
    expenses.clear()
    total_label.config(text="Total Expense: ₹0")
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)        

add_button = tk.Button(window, text="Add Expense", font=("Arial", 14, "bold"), bg="green", fg="white", command=add_expense)  
add_button.pack(pady=10)

expense_list = tk.Listbox(window, width=40, height=8, font=("Arial", 12))
expense_list.pack(pady=10)

total_label = tk.Label(window, text="Total Expense: ₹0", font=("Arial", 14, "bold"), bg="#87CEEB", fg="darkblue")
total_label.pack(pady=10)

clear_button = tk.Button(window, text="Clear All", font=("Arial", 14, "bold"), bg="red", fg="white", command=clear_all)
clear_button.pack(pady=10)

window.mainloop()