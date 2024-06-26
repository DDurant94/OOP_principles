# This module takes in your budget name and sets a value that you want to use. Not letting you go below 0 but subtracting down to 0 from the amount
# that you had stated allowing you to add expenses to that value till 0 
class BudgetCategory:
  def __init__(self,name,allocated_budget):
    self.__name = name
    self._allocated_budget = max(0,allocated_budget)

  def get_name(self):
    return self.__name
  
  def set_name(self,new_name):
    self.__name = new_name

  def get_allocation(self):
      return self._allocated_budget
    
  def set_allocation(self,new_amount):
    if new_amount >= 0:
            self._allocated_budget = new_amount
    else:
       print("Enter a positive amount")
  
  def add_expenses(self, amount):
    if amount >= 0:
      if amount <= self._allocated_budget:
        self._allocated_budget -= amount
        print(f"Expense of ${amount:.2f} added to {self.__name}.")
      else:
         print("You Don't have enough money for this")
    else:
      print("Enter a positive amount")      

  def display_category_summary(self):
    print(f"Category: {self.__name}")
    print(f"Remaining Budget: ${self.get_allocation():.2f}") 