import tkinter as tk

window = tk.Tk()
window.title("Invoice Billing System")
window.geometry("500x650")
window.config(bg="#D8BFD8")

heading = tk.Label(window, text="Invoice Billing System", font=("Arial", 22, "bold"), bg="#D8BFD8", fg="purple")
heading.pack(pady=20)

customer_label = tk.Label(window, text="Customer Name", font=("Arial", 14), bg="#D8BFD8")
customer_label.pack()
customer_entry = tk.Entry(window, font=("Arial", 14), width=25)
customer_entry.pack(pady=5)

product_label = tk.Label(window, text="Product Name", font=("Arial", 14), bg="#D8BFD8")
product_label.pack()
product_entry = tk.Entry(window, font=("Arial", 14), width=25)
product_entry.pack(pady=5)

quantity_label = tk.Label(window, text="Quantity", font=("Arial", 14), bg="#D8BFD8")
quantity_label.pack()
quantity_entry = tk.Entry(window, font=("Arial", 14), width=25)
quantity_entry.pack(pady=5)

price_label = tk.Label(window, text="Price", font=("Arial", 14), bg="#D8BFD8")
price_label.pack()
price_entry = tk.Entry(window, font=("Arial", 14), width=25)
price_entry.pack(pady=5)

def generate_bill():
    customer = customer_entry.get()
    product = product_entry.get()
    quantity = int(quantity_entry.get())
    price = int(price_entry.get())
    total = quantity * price
    bill_text.config(text=f"""
Customer: {customer}
Product: {product}
Quantity: {quantity}
Price: ₹ {price}
Total Bill: ₹ {total}
""")

def clear_bill():
    customer_entry.delete(0, tk.END)
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    bill_text.config(text="Your Bill Appear Here")


generate_button = tk.Button(window, text="Generate Bill", font=("Arial", 14, "bold"), bg="green", fg="white", command=generate_bill)
generate_button.pack(pady=15)

bill_text = tk.Label(window, text="Your Bill Will Appear Here", font=("Arial", 13), bg="#D8BFD8", fg="darkblue", justify="left")
bill_text.pack(pady=10)

clear_button = tk.Button(window, text="Clear Bill", font=("Arial", 14, "bold"), bg="red", fg="white", command=clear_bill)
clear_button.pack(pady=10)
window.mainloop()

 