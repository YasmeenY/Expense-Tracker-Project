from expense import Expense
from earnings import Earnings
from compare import compare

import sqlite3

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

EXPENSE_CATEGORIES = ["Food", "Clothes", "Travel", "Utilities", "Rent", "Misc.", "Bills"]

while True:
    try:
        print("Select an option:")
        print("1. Expenses")
        print("2. Earnings")
        print("3. Compare Expenses and Earnings")

        choice = int(input("Pick a Number:"))

        if choice == 1:
            print("1. View Total Expenses in each category")
            print("2. Add New Expense")
            print("3. Remove Expense")
            print("4. View Total expenses in each category")

            expense_choice = int(input("Pick a Number:"))

            if expense_choice == 1:
                category = input("Which category do you want to see? Food, Clothes, Travel, Utilities, Rent, Misc. or Bills ? ")
                print(Expense.find_by_category(category))
            elif expense_choice == 2:
                name = input("What did you buy: ")
                category = input("What category was it ? Food, Clothes, Travel, Utilities, Rent, Misc. or Bills ? ")
                price = float(input("How much did you spend: "))
                Expense.create(name, category, price)
            elif expense_choice == 3:
                name = input("What expense do you want to remove: ")
                category = input("What category was it ? Food, Clothes, Travel, Utilities, Rent, Misc. or Bills ? ")
                Expense.delete(name, category)
            elif expense_choice == 4:
                Expense.total()
            else:
                print("Invalid Choice Exit")
                exit()

        elif choice == 2:
            print("1. View Total Earnings in each category")
            print("2. Add New Earning")
            print("3. Remove Earning")
            print("4. View Total earnings in each category")

            earning_choice = int(input("Pick a Number:"))

            if earning_choice == 1:
                category = input("Which category do you want to see? Passive Income, Salary, Freelance, Gifts ? ")
                print(Earnings.find_by_category(category))
            elif earning_choice == 2:
                name = input("Where are the earning from?: ")
                category = input("What category was it ? Passive Income, Salary, Freelance, Gifts ? ")
                amount = float(input("How much did you earn: "))
                Earnings.create(name, category, amount)
            elif earning_choice == 3:
                name = input("What earning do you want to remove: ")
                category = input("What category was it ? Passive Income, Salary, Freelance, Gifts ? ")
                Earnings.delete(name, category)
            elif earning_choice == 4:
                Earnings.total()
            else:
                print("Invalid Choice Exit")
                exit()

        elif choice == 3:
            print(compare())

        else:
            print("Invalid Choice Exit")
            exit()

        # Ask the user if they want to continue or exit the program
        continue_choice = int(input("\nWould you like to do something else? Pick 1 to return to the main menu or 0 to exit: "))

        if continue_choice == 1:
            continue
        elif continue_choice == 0:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Exiting the program. Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

