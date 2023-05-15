from expense import Expense
import sqlite3


CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

while True:
    print("Select an option:")
    print("1. Expenses")
    print("2. Earnings")

    choice = int(input("Pick a Number:"))

    if choice == 1:
        print("1. View Total Expenses in each category")
        print("2. Add New Expense")
        print("3. Add New Expense")
        print("4. Remove Expense")

        expense_choice = int(input("Pick a Number:"))

        if expense_choice == 2:
            category = input("What category is it ? Food, Clothes, Travel, Utilities, Rent, Misc. or Bills ? ")
            Expense.find_by_category(category)
            exit()
        elif expense_choice == 3:
            name = input("What did you buy: ")
            category = input("What category was it ? Food, Clothes, Travel, Utilities, Rent, Misc. or Bills ? ")
            price = input("How much did you spend: ")
            Expense.create(name, category, price)

            continue_choice = int(input("Pick 1 to return to main menu or press 0 to exit: "))

            if (continue_choice) == 1:
                continue
            if (continue_choice) == 0:
                exit()
            else:
                print("Invalid Choice Exit")
                exit()
        elif earning_choice == 1:
            print("View Total Expenses in each category")
            exit()
        elif earning_choice == 4:
            print("Remove Expense")
            exit()
        else:
            print("Invalid Choice Exit")
            exit()

    elif choice == 2:
        print("1. View Total Earnings in each category")
        print("2. View Earnings By Category")
        print("3. Add New Earning")
        print("4. Remove Expense")

        earning_choice = int(input("Pick a Number:"))

        if earning_choice == 1:
            print("View Total Earnings in each category")
            exit()
        elif earning_choice == 3:
            print("Add Earning")
            continue_choice = int(input("Pick 1 to return to main menu or press 0 to exit: "))
            
            if (continue_choice) == 1:
                continue
            if (continue_choice) == 0:
                exit()
            else:
                print("Invalid Choice Exit")
                exit()
        elif earning_choice == 2:
            print("View Earnings By Category")
            exit()
        elif earning_choice == 4:
            print("Remove Expense")

        else:
            print("Invalid Choice Exit")
            exit()

    else:
        print("Invalid Choice Exit")
        exit()
        