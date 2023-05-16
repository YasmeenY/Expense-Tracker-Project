from expense import Expense
from earnings import Earnings
from users import Users

def add_to_db():
    Users.create("Dede", "Do", "Bye")
    Users.create("Mimi", "Mo", "nay")
    Users.create("Yoyo", "Yo", "day")

    Expense.create("Milk", "Food", 7, "2023-02-01", 1)
    Expense.create("Snacks", "Food", 20, "2023-03-01", 1)
    Expense.create("Bread", "Food", 4, "2023-06-01", 1)
    Expense.create("Gas", "Bills", 140, "2023-07-01", 1)

    Expense.create("Milk", "Food", 7, "2023-02-01", 2)
    Expense.create("Snacks", "Food", 20, "2023-03-01", 2)
    Expense.create("Party", "Entertainment", 400, "2023-06-01", 2)
    Expense.create("Apartment Rent", "Rent", 2100, "2023-07-01", 2)
    Expense.create("Utilities", "Utilities", 700, "2023-07-01", 2)

    Earnings.create("Gifts", "Gifts", 100, "2023-02-01", 1)
    Earnings.create("Income", "Income", 3000, "2023-03-01", 1)

    Earnings.create("Gifts 2", "Gifts", 100, "2023-02-01", 2)
    Earnings.create("Income", "Income", 3000, "2023-06-01", 2)

    Expense.create("Bread", "Food", 7, "2023-02-01", 2)
    Earnings.create("Gifts 3", "Gifts", 7, "2023-02-01", 2)
