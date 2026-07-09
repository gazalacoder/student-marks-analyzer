import tkinter as tk
from tkinter import messagebox

students = []

def calculate_percentage():
    marks = float(marks_entry.get())
    percentage = (marks / 100) * 100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B" 
    elif percentage >= 60:
        grade = "C" 
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"             
    result_label.config(text=f"Percentage: {percentage}% | Grade: {grade}")

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)     

def save_record():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()
    if name and roll and marks:
        data = f"Name {name} | Roll No: {roll} | Marks: {marks}" 
        students.append(data)
        records_list.insert(tk.END, data)
        with open("student_records.txt", "a") as file:
            file.write(data + "\n")
            messagebox.showinfo("Success", "Student Record Saved Successfully!")
            clear_fields()
    else:
        messagebox.showerror("Error", "Please fill all fields!")

def search_student():
    search = name_entry.get().lower()
    records_list.delete(0, tk.END)
    found = False
    for student in students:
        if search in student.lower():
            records_list.insert(tk.END, student)
            found = True
            if not found:
                messagebox.showinfo("Search", "Student Not Found!")

window = tk.Tk()
window.title("Student Management System")
window.geometry("700x600")
window.config(bg="#D6EAF8")

heading = tk.Label(window, text="Student Management System", font=("Arial", 20, "bold"), bg="#D6EAF8", fg="darkblue")
heading.pack(pady=15)

name_label = tk.Label(window, text="Student Name:", font=("Arial", 12), bg="#D6EAF8")
name_label.pack()
name_entry =  tk.Entry(window, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

roll_label = tk.Label(window, text="Roll Number:", font=("Arial", 12, "bold"), bg="#D6EAF8")
roll_label.pack()
roll_entry = tk.Entry(window, width=30, font=("Arial", 12))
roll_entry.pack(pady=5)

marks_label = tk.Label(window, text="Marks:", font=("Arial", 12, "bold"), bg="#D6EAF8")
marks_label.pack()
marks_entry = tk.Entry(window, width=30, font=("Arial", 12))
marks_entry.pack(pady=5)

calulate_button = tk.Button(window, text="Calculate Percentage", font=("Arial", 12, "bold"), bg="green", fg="white", command=calculate_percentage)
calulate_button.pack(pady=10)

result_label = tk.Label(window, text="Percentage", font=("Arial", 12, "bold"), bg="#D6EAF8", fg="darkblue")
result_label.pack(pady=10)

save_button = tk.Button(window, text="Saved Record", font=("Arial", 12, "bold"), bg="blue", fg="white", command=save_record)
save_button.pack(pady=10)

search_button = tk.Button(window, text="Search Student", font=("Arial", 12, "bold"), bg="purple", fg="white", command=search_student)
search_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear Fields", font=("Arial", 12, "bold"), bg="orange", fg="white", command=clear_fields)
clear_button.pack(pady=5)

records_label = tk.Label(window, text="Student Records", font=("Arial", 12, "bold"), bg="#D6EAF8")
records_label.pack(pady=5)

records_list = tk.Listbox(window, width=70, height=8, font=("Arial", 11))
records_list.pack(pady=10)

window.mainloop()


