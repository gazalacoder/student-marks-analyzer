import csv
import os
FILE_NAME = "students.csv"
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="")as file:
            writer = csv.writer(file)
            writer.writerow(["Name","Marks"])

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    with open(FILE_NAME, "a", newline="")as file:
        writer = csv.writer(file)
        writer.writerow([name, marks])
    print("Student added successfully!")

def view_students():
    print("\n Student List:\n")
    with open(FILE_NAME, "r")as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def delete_student():
    name = input("Enter student name to delete: ")
    updated_data = []
    found = False

    with open(FILE_NAME, "r")as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                updated_data.append(row)
            else:
                found = True
    with open(FILE_NAME, "w", newline="")as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)
    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def menu():
    create_file()
    while True:
        print("\n====== CSV STUDENT MANAGER======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting program...")
        else:
            print("Invalid choice! Try again.")
        menu()
        
        
        
