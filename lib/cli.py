import datetime
from expense import Expense
from earnings import Earnings
from users import Users
from compare import compare
from compare import warn_user
import getpass

#checks if it is in proper date time format
def valid_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def valid_string(name):
    if len(name) >= 1:
        return True
    else:
        return False

def display_category(current_category):
    if current_category != [] and len(current_category) != 1:
        print ('\033[94mYour current categories are '+', '.join(current_category[:-1]) + ' & ' + current_category[-1] + "\033[00m")
    elif len(current_category) == 2:
        print ('\033[94mYour current categories are '+ " & ".join(current_category) + "\033[00m")
    elif len(current_category) == 1:
        print("\033[94m" + "".join(current_category) + "\033[00m")
    else:
        print("\033[94mYou currently have no categories\033[00m")
    

# Ask the user if they want to continue or exit the program
def exit_or_continue():
    if choice == 4:
        return

    continue_choice = input("\n\033[91mWould you like to do something else ? Press 0 to exit or press any other button to return to main menu. \033[00m")

    if continue_choice == "0":
        print("\033[95mExiting the program. Goodbye! \033[00m")
        exit()

##asks for user information
def user_sign_in():
    first_name = input("\033[94mEnter Your first name: \033[00m").lower().capitalize()
    last_name = input("\033[94mEnter Your last name: \033[00m").lower().capitalize()
    user_exist = Users.check_if_user_exists(first_name, last_name)
    if user_exist == False:
        print("\033[95mUser doesn't exist creating new user...\033[00m")
        password = getpass.getpass("\033[94mEnter New password: \033[00m")
        Users.create(first_name, last_name, password)
    else:
        password = getpass.getpass("\033[94mEnter password: \033[00m")
        password_check = Users.get_password(first_name, last_name)
        count = 1
        while password != password_check:
                if count != 3:
                    count +=1
                    password = getpass.getpass("\033[93mIncorrect password please try again: \033[00m")
                else:
                    print("\033[91mSorry Password wrong 3 times Goodbye!\033[00m")
                    exit()
            
        print(f"\n\n\033[95m\U0001F973 Hello {first_name} what would you like to do today?\U0001F973\n\033[00m")

    global user_id
    user_id = Users.get_id(first_name, last_name)[0]


user_sign_in()

#beginning of cli loop
while True:
    try:
        print("\nSelect an option:")
        print("\033[91m1. Expenses\033[00m")
        print("\033[92m2. Earnings\033[00m")
        print("\033[93m3. Compare Earnings and Expenses\033[00m")
        print("\033[95m4. Change User\033[00m")
        print("\033[91m5. Delete user\033[00m")
        print("\033[90m6. Exit\n\033[00m")

        choice = int(input("\033[94mPick a Number: \033[00m"))

        #view add or remove expenses
        if choice == 1:
            print("\n\n\033[91m1. View Total Expenses in each category")
            print("2. Add New Expense")
            print("3. View Expenses By Date")
            print("4. Remove Expense\n\033[00m")

            expense_choice = int(input("\033[94mPick a Number: \033[00m"))
            print("\n")

            while expense_choice != 1 and expense_choice != 2 and expense_choice != 3 and expense_choice != 4:
                expense_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))
                print("\n")

            #View total expenses and gets choice to view each item in a specific category
            if expense_choice == 1:
                Expense.view_total_expenses(user_id)
                view_specific = input("\n\033[94mWould you like to see the total expense of specific category? Y/N. \033[00m")
                if view_specific.lower() == 'y':
                    category = input("\n\033[94mEnter the category: \033[00m").lower().capitalize()
                    while not valid_string(category):
                        print("\n\033[93mInvalid category. Please try again.")
                        category = input("\033[94mEnter the category: \033[00m")
                    expenses = Expense.view_expense_by_category(category, user_id)
                    print("\n")
                    print(expenses)

            #for adding a new expense
            elif expense_choice == 2:
                name = input("\033[94mWhat did you buy: \033[00m")
                while not valid_string(name):
                    print("\n\033[93mInvalid name. Please try again.")
                    name = input("\033[94mWhat did you buy: \033[00m")
                print("\033[94mWhat category was it ?\033[00m")
                current_category = list(Expense.find_user_categories(user_id))
                display_category(current_category)
                category = input("\n\033[94mItem category: \033[00m").lower().capitalize()
                while not valid_string(category):
                    print("\n\033[93mInvalid category. Please try again.")
                    category = input("\033[94mItem category: \033[00m")
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

            #View expenses by date
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
            #Removing an expense by id
            elif expense_choice == 4:
                current_category = list(Expense.find_user_categories(user_id))
                if current_category == []:
                    print("\033[93mYou have nothing to remove\033[00m")
                else:
                    display_category(current_category)
                    category = input("\n\033[94mEnter the category of the item you want to remove: \033[00m").lower().capitalize()
                    while not valid_string(category):
                        print("\n\033[93mInvalid category. Please try again.")
                        category = input("\n\033[94mEnter the category of the item you want to remove: \033[00m").lower().capitalize()
                    expenses = Expense.view_expense_by_category(category, user_id)
                    print("\n")
                    print(expenses)
                    try:
                        id = int(input("\n\033[94mEnter the id of the expense to remove: \033[00m"))
                    except ValueError:
                        id = input("\n\033[94mEnter the id of the expense to remove: \033[00m")
                    Expense.remove(id)
                    print(f"\n\033[92mSuccessfully removed ID #{id}\033[00m")

        #view add or remove earnings
        elif choice == 2:
            print("\n\n\033[92m1. View Total Earnings in each category")
            print("2. Add New Earning")
            print("3. View Earnings By Date")
            print("4. Remove Earning\033[00m\n")


            earning_choice = int(input("\033[94mPick a Number: \033[00m"))
            print("\n")
            while earning_choice != 1 and earning_choice != 2 and earning_choice != 3 and earning_choice != 4:
                earning_choice = int(input("\033[94mInvalid choice please choose again: \033[00m"))

            #View total earnings gets choice to view each item in a specific category
            if earning_choice == 1:
                Earnings.view_total_earnings(user_id)
                view_specific = input("\n\033[94mWould you like to see the total earnings of a specific category? Y/N. \033[00m")
                if view_specific.lower() == 'y':
                    category = input("\n\033[94mEnter the category: \033[00m").lower().capitalize()
                    while not valid_string(category):
                        print("\n\033[93mInvalid category. Please try again.")
                        category = input("\033[94mEnter the category: \033[00m")
                    earnings = Earnings.view_earnings_by_category(category, user_id)   
                    print("\n")
                    print(earnings)         

            #for adding a new earning
            elif earning_choice == 2:
                source = input("\033[94mWhat was the source of the earning: \033[00m")
                while not valid_string(source):
                    print("\n\033[93mInvalid Source. Please try again.\033[00m")
                    start_date = input("\033[94mWhat was the source of the earning: \033[00m")
                print("\033[94mWhat category was it ?")
                current_category = list(Earnings.find_user_categories(user_id))
                display_category(category)
                category = input("\n\033[94mItem category: \033[00m").lower().capitalize()
                while not valid_string(category):
                    print("\n\033[93mInvalid category. Please try again.\033[00m")
                    start_date = input("\033[94mItem category: \033[00m")
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
                    date = input("\n\033[94mEnter the date of the transaction (YYYY-MM-DD): \033[00m")
                Earnings.create(source, category, amount, date, user_id)
            
            #for view earnings by date
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
            #remove earning by id
            elif earning_choice == 4:
                current_category = list(Earnings.find_user_categories(user_id))
                if current_category == []:
                    print("\033[93mYou have nothing to remove\033[00m")
                else:
                    display_category(current_category)
                    category = input("\n\033[94mEnter the category of the item you want to remove: \033[00m").lower().capitalize()
                    while not valid_string(category):
                        print("\n\033[93mInvalid category. Please try again.")
                        category = input("\n\033[94mEnter the category of the item you want to remove: \033[00m").lower().capitalize()
                    earnings = Earnings.view_earnings_by_category(category, user_id)   
                    print("\n")
                    print(earnings)
                    try:
                        id = int(input("\n\033[94mEnter the id of the earning to remove: \033[00m"))
                    except ValueError:
                        id = input("\n\033[94mEnter the id of the earning to remove: \033[00m")
                    Earnings.remove(id)
                    print(f"\n\033[92mSuccessfully removed ID #{id}\033[00m")

        #compare between earnings and expenses
        elif choice == 3:
            print(compare(user_id))
        #change user
        elif choice == 4:
            print("\n\n\n\033[92m---Changing User---\033[00m\n")
            user_sign_in()
        #deletes user
        elif choice == 5:
            confirm_choice = input("\033[91mAre you sure you wish to delete the user press 0 to confirm deletion or any other button to return to main menu: ")
            if confirm_choice == "0":
                Users.delete_user(user_id)
                print("Deleting user... \U0001F641")
                print("Exiting now...\033[00m")
                exit()
            else:
                continue
        #exit cli
        elif choice == 6:
            print("\033[95mExiting now Goodbye! \033[00m")
            exit()
        else:
            print("\033[94mInvalid choice please choose again: \033[00m")
            continue

        #asks user if they want to got to main menu or exit after each completed operation
        exit_or_continue()

    except ValueError:
        choice = input("\033[94mInvalid number please pick a valid number or return to main menu: \033[00m")
