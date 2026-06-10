balance = 0
while True:
    print("\n===== EXPENSE TACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        income = float(input("Enter income: "))
        balance += income
        print("Income Added!")
    elif choice == "2":
        expense = float(input("Enter expense:"))
        balance -= expense
        print("Expense Added")
    elif choice == "3":
        print("Current Balance:", balance)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice")
        
                       
