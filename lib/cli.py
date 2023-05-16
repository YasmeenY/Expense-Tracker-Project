import datetime
from expense import Expense
from earnings import Earnings
from users import Users
from compare import compare
from compare import warn_user
import sqlite3
import getpass

def valid_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()


def user_sign_in():
    first_name = input("\033[94mEnter Your first name: \033[00m").lower().capitalize()
    last_name = input("\033[94mEnter Your last name: \033[00m").lower().capitalize()
    password = getpass.getpass("\033[94mEnter password: \033[00m")
    Users.create(first_name,last_name, password)
    password_check = Users.get_password(first_name, last_name)
    count = 1
    while password != password_check:
            if count != 3:
                count +=1
                password = getpass.getpass("\033[93mIncorrect password please try again: \033[00m")
            else:
                print("\033[91mSorry Password wrong 3 times Goodbye!\033[00m")
                exit()
        
    print(f"\n\n\U0001F973\033[95m Hello {first_name} what would you like to do today? \U0001F973\n\033[00m")

    global user_id
    user_id = Users.get_id(first_name, last_name)

user_sign_in()

while True:
    try:
        print("\nSelect an option:")
        print("\033[91m1. Expenses\033[00m")
        print("\033[92m2. Earnings\033[00m")
        print("\033[93m3. Compare Earnings and Expenses\033[00m")
        print("\033[95m4. Change User\033[00m")
        print("\033[90m5. Exit\n\033[00m")

        choice = int(input("\033[94mPick a Number: \033[00m"))

        if choice == 1:
            print("\n\n\033[91m1. View Total Expenses in each category")
            print("2. Add New Expense")
            print("3. View Expenses By Date")
            print("4. Remove Expense\n\033[00m")

            expense_choice = int(input("\033[94mPick a Number: \033[00m"))
            print("\n")

            while expense_choice != 1 and expense_choice != 2 and expense_choice != 3 and expense_choice != 4:
                expense_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))

            if expense_choice == 1:
                Expense.view_total_expenses(user_id)
                view_specific = input("\n\033[94mWould you like to see the total expense of specific category? Y/N. \033[00m")
                if view_specific.lower() == 'y':
                    category = input("\n\033[94mEnter the category: \033[00m").lower().capitalize()
                    Expense.view_expense_by_category(category, user_id)

                # Ask the user if they want to continue or exit the program
                continue_choice = int(input("\n\033[91mWould you like to do something else? Pick 1 to return to the main menu or 0 to exit: \033[00m"))

                while continue_choice != 1 and continue_choice != 0:
                    continue_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))

                if continue_choice == 1:
                    continue
                elif continue_choice == 0:
                    print("\033[95mExiting the program. Goodbye! \033[00m")
                    break


            elif expense_choice == 2:
                name = input("\033[94mWhat did you buy: \033[00m")
                print("\033[94mWhat category was it ?\033[00m")
                current_category = list(Expense.find_user_categories(user_id))
                if current_category != [] and len(current_category) != 1:
                    print ('\033[94mYour current categories are '+', '.join(current_category[:-1]) + ' & ' + current_category[-1] + "\033[00m")
                elif len(current_category) == 2:
                    print ('\033[94mYour current categories are '+ " & ".join(current_category) + "\033[00m")
                elif len(current_category) == 1:
                    print("\033[94m" + "".join(current_category) + "\033[00m")
                else:
                    print("\033[94mYou currently have no categories\033[00m")
                category = input("\n\033[94mItem category: \033[00m").lower().capitalize()
                while True:
                    try:
                        price = float(input("\n\033[94mHow much did you spend: \033[00m"))
                    except ValueError:
                        print("\033[93mPrice was not a float number please try again: \033[00m")
                        continue
                    else:
                        break
                date = input("\n\033[94mEnter the date of the transaction (YYYY-MM-DD): \033[00m")
                while not valid_date(date):
                    print("\n\033[93mInvalid date. Please try again.")
                    date = input("\n\033[94mEnter the date of the transaction (YYYY-MM-DD): \033[00m")
                Expense.create(name, category, price, date, user_id)
                print("\n" + warn_user(user_id))
            elif expense_choice == 3:
                start_date = input("\033[94mEnter the start date (YYYY-MM-DD): \033[00m")
                while not valid_date(start_date):
                    print("\n\033[93mInvalid Start date. Please try again.\033[00m")
                    start_date = input("\033[94mEnter the start date (YYYY-MM-DD): \033[00m")
                end_date = input("\033[94mEnter the end date (YYYY-MM-DD): \033[00m")
                while not valid_date(end_date):
                    print("\n\033[93mInvalid End date. Please try again.\033[00m")
                    end_date = input("\033[94mEnter the end date (YYYY-MM-DD): \033[00m")
                expenses = Expense.find_by_date(start_date, end_date, user_id)
                print("\n")
                print(expenses)
            elif expense_choice == 4:
                id = int(input("\033[94mEnter the id of the expense to remove: \033[00m"))
                Expense.remove(id)

            # Ask the user if they want to continue or exit the program
            continue_choice = int(input("\n\033[91mWould you like to do something else? Pick 1 to return to the main menu or 0 to exit: \033[00m"))

            while continue_choice != 1 and continue_choice != 0:
                continue_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))

            if continue_choice == 1:
                continue
            elif continue_choice == 0:
                print("\033[95mExiting the program. Goodbye! \033[00m")
                break

        elif choice == 2:
            print("\n\n\033[92m1. View Total Earnings in each category")
            print("2. Add New Earning")
            print("3. View Earnings By Date")
            print("4. Remove Earning\033[00m")
            print("\033[93m4. Change User\033[00m")
            print("\033[93m5. Exit\n\033[00m")

            earning_choice = int(input("\033[94mPick a Number: \033[00m"))
            print("\n")
            while earning_choice != 1 and expense_choice != 2 and expense_choice != 3 and expense_choice != 4:
                earning_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))

            if earning_choice == 1:
                Earnings.view_total_earnings(user_id)
                view_specific = input("\033[94mWould you like to see the total earnings of a specific category? Y/N. \033[00m")
                if view_specific.lower() == 'y':
                    category = input("\033[94mEnter the category: \033[00m").lower().capitalize()
                    Earnings.view_earnings_by_category(category, user_id)
                continue
            elif earning_choice == 2:
                source = input("\033[94mWhat was the source of the earning: \033[00m")
                print("\033[94mWhat category was it ?")
                current_category = list(Earnings.find_user_categories(user_id))
                if current_category != [] and len(current_category) != 1:
                    print ('\033[94mYour current categories are '+', '.join(current_category[:-1]) + ' & ' + current_category[-1] + "\033[00m")
                elif len(current_category) == 2:
                    print ('\033[94mYour current categories are '+ " & ".join(current_category) + "\033[00m")
                elif len(current_category) == 1:
                    print("\033[94m" + "".join(current_category) + "\033[00m")
                else:
                    print("\033[94mYou currently have no categories\033[00m")
                category = input("\n\033[94mItem category: \033[00m").lower().capitalize()
                while True:
                    try:
                        amount = float(input("\n\033[94mHow much did you earn: \033[00m"))
                    except ValueError:
                        print("\033[93mAmount was not a float number please try again. \033[00m")
                        continue
                    else:
                        break
                date = input("\n\033[94mEnter the date of the transaction (YYYY-MM-DD): \033[00m")
                while not valid_date(date):
                    print("\033[93mInvalid date. Please try again.\033[00m")
                    continue
                Earnings.create(source, category, amount, date, user_id)
            elif earning_choice == 3:
                start_date = input("\033[94mEnter the start date (YYYY-MM-DD): \033[00m")
                while not valid_date(start_date):
                    print("\n\033[93mInvalid Start date. Please try again.")
                    start_date = input("\033[94mEnter the start date (YYYY-MM-DD): \033[00m")
                end_date = input("\033[94mEnter the end date (YYYY-MM-DD): \033[00m")
                while not valid_date(end_date):
                    print("\n\033[93mInvalid End date. Please try again.")
                    end_date = input("\033[94mEnter the end date (YYYY-MM-DD): \033[00m")
                earnings = Earnings.find_by_date(start_date, end_date, user_id)
                print("\n")
                print(earnings)
            elif earning_choice == 4:
                id = int(input("\033[94mEnter the id of the earning to remove: \033[00m"))
                Earnings.remove(id)
            
            # Ask the user if they want to continue or exit the program
            continue_choice = int(input("\n\033[91mWould you like to do something else? Pick 1 to return to the main menu or 0 to exit: \033[00m"))

            while continue_choice != 1 and continue_choice != 0:
                continue_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))

            if continue_choice == 1:
                continue
            elif continue_choice == 0:
                print("\033[95mExiting the program. Goodbye! \033[00m")
                break


        elif choice == 3:
            print(compare(user_id))
        elif choice == 4:
            print("\n\n\n\033[92m---Changing User---\033[00m\n")
            user_sign_in()
        elif choice == 5:
            print("\033[95mExiting now Goodbye! \033[00m")
            exit()
        else:
            print("\033[94mInvalid choice please choose again: \033[00m")
            continue

        # Ask the user if they want to continue or exit the program
        continue_choice = int(input("\n\033[91mWould you like to do something else? Pick 1 to return to the main menu or 0 to exit: \033[00m"))
        while continue_choice != 1 and continue_choice != 0:
            continue_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))
        if continue_choice == 1:
            continue
        elif continue_choice == 0:
            print("\033[95mExiting the program. Goodbye! \033[00m")
            break

    except ValueError:
        print("\033[94mInvalid choice please choose again: \033[00m")
        continue

CONN.close()

