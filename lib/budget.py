from cli import Expense

class Budget(Expense):

  def __init__(self, name, category, amount):
    super().__init__(name, category, amount)

  def __repr__(self):
    return f"Budget({self.name}, {self.category}, {self.amount})"

def create_budget():
  name = input("What is the name of the budget? ")
  category = input("What category is the budget for? ")
  amount = float(input("What is the amount of the budget? "))

  budget = Budget(name, category, amount)
  db.session.add(budget)
  db.session.commit()

  print(f"Budget {budget.name} created successfully.")

def list_budgets():
  budgets = Budget.query.all()

  for budget in budgets:
    print(f"Budget: {budget.name} | Category: {budget.category} | Amount: {budget.amount}")

def track_spending():
  expenses = Expense.query.all()

  for expense in expenses:
    budget = Budget.query.filter_by(name=expense.category).first()

    if budget is not None:
      budget.amount -= expense.amount
      db.session.commit()

def send_notifications():
  budgets = Budget.query.all()

  for budget in budgets:
    if budget.amount < 0:
      print(f"Budget {budget.name} is over budget!")