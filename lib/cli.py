import datetime
from expense import Expense
from earnings import Earnings
from compare import compare
import sqlite3

def valid_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

while True:
    print("Select an option:")
    print("1. Expenses")
    print("2. Earnings")
    print("3. Compare Earnings and Expenses")

    choice = int(input("Pick a Number:"))

    if choice == 1:
        print("1. View Total Expenses in each category")
        print("2. Add New Expense")
        print("3. View Expenses By Date")
        print("4. Remove Expense")

        expense_choice = int(input("Pick a Number:"))

        if expense_choice == 1:
            Expense.view_total_expenses()
            view_specific = input("Would you like to see the total expense of specific category? Y/N. ")
            if view_specific.lower() == 'y':
                category = input("Enter the category: ")
                Expense.view_expense_by_category(category)
            continue
        elif expense_choice == 2:
            name = input("What did you buy: ")
            category = input("What category was it ? Food, Clothes, Travel, Utilities, Rent, Misc. or Bills ? ")
            price = float(input("How much did you spend: "))
            date = input("Enter the date of the transaction (YYYY-MM-DD): ")
            if not valid_date(date):
                print("Invalid date. Please try again.")
                continue
            Expense.create(name, category, price, date)
        elif expense_choice == 3:
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            if not valid_date(start_date) or not valid_date(end_date):
                print("Invalid date. Please try again.")
                continue
            expenses = Expense.find_by_date(start_date, end_date)
            print(expenses)
        elif expense_choice == 4:
            id = int(input("Enter the id of the expense to remove: "))
            Expense.remove(id)
        else:
            print("Invalid Choice. Exiting.")
            break
    elif choice == 2:
        print("1. View Total Earnings in each category")
        print("2. Add New Earning")
        print("3. View Earnings By Date")
        print("4. Remove Earning")

        earning_choice = int(input("Pick a Number:"))

        if earning_choice == 1:
            Earnings.view_total_earnings()
            view_specific = input("Would you like to see the total earnings of a specific category? Y/N. ")
            if view_specific.lower() == 'y':
                category = input("Enter the category: ")
                Earnings.view_earnings_by_category(category)
            continue
        elif earning_choice == 2:
            source = input("What was the source of the earning: ")
            category = input("What category was it ? Passive Income, Salary, Freelance, Gifts ? ")
            amount = float(input("How much did you earn: "))
            date = input("Enter the date of the transaction (YYYY-MM-DD): ")
            if not valid_date(date):
                print("Invalid date. Please try again.")
                continue
            Earnings.create(source, category, amount, date)
        elif earning_choice == 3:
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            if not valid_date(start_date) or not valid_date(end_date):
                print("Invalid date. Please try again.")
                continue
            earnings = Earnings.find_by_date(start_date, end_date)
            print(earnings)
        elif earning_choice == 4:
            id = int(input("Enter the id of the earning to remove: "))
            Earnings.remove(id)
        else:
            print("Invalid Choice. Exiting.")
            break
    elif choice == 3:
        print(compare())
    else:
        print("Invalid Choice. Exiting.")
        break

CONN.close()

