# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:59:27 2022

@author: Dalang, Felix Sihitshuwam
"""

class Simulator:
  def __init__(self, coffee, milk, cups, sugar):
    """
    """
    self.coffee = coffee
    self.milk = milk
    self.cups = cups
    self.sugar = sugar
    self.cost_with_sugar = 85
    self.cost_with_no_sugar = 80
    self.state = False
  
  def switch(self, flag=True):
    """
    Switch on Simulator On/Off

    Args:
      flag (TYPE, optional): DESCRIPTION. Defaults to True.

    Returns:
      None.

    """
    self.state = flag
  
  def console(self):
    """
    Console which displays services provided by machine.

    Returns:
      None.

    """
    while True:
      self.console_output()
      code = input()
      if code == '1':
        self.order()
      elif code == '2' :
        self.display_stock()
      elif code == '3':
        self.refresh_()
      elif code == 'q':
        self.switch(False)
        break
      else:
        print("Invalid Input")
        
    
  
  def order(self):
    """
    First checks to see if there are empty ingredients or items.
    """
    
    if self.notify_empty():
      return
    
    self.coffee -= 1
    self.milk -= 1
    self.cups -= 1
    
    while True:
      sugar = input("Will you want sugar to be added? (Y or N): ")
      if not sugar.upper() in ('Y', 'N'):
        print("Invalid Input")
      else:
        break
    
    cost = self.cost_with_no_sugar
    if sugar == 'Y':
      self.sugar -= 1
      cost = self.cost_with_sugar
    
    print()
    print(f"You will pay {cost}rubs for your coffee. Please, place your card on the screen then press enter.")
    input()
    print("Here is your coffee. Bye Bye!")
  
  def display_stock(self):
    """"""
    print("#"*50)
    print(f"Coffee:\t{self.coffee}\nMilk:\t{self.milk}\nCups:\t{self.cups}\nSugar:\t{self.sugar}")
    print("#"*50)
  
  def notify_empty(self, details=False):
    """
    

    Args:
      details (TYPE, optional): Whether to say which item is finished or not. 
      Defaults to False.

    Returns:
      None.

    """
    if 0 in (self.sugar, self.milk, self.cups, self.coffee):
      print("#"*46)
      print("##\t\tAlert, we are out of some stock\t\t##")
      print("#"*46)
      return True
    return False
  
  def refresh_(self):
    """
    Upgrade stocks.

    Returns:
      None.

    """
    print("Enter the quantity for each item. Enter 0 when nothing is being added.")
    coffee = int(input('coffee: '))
    milk = int(input('milk: '))
    cups = int(input('cups: ')) 
    sugar = int(input('sugar: '))
    
    self.coffee += coffee
    self.milk += milk
    self.cups += cups
    self.sugar += sugar
    
  def console_output(self):
    print()
    print("#"*50)
    print("Press 1 to order coffee\n"
          "Press 2 to display the amount of supplies.\n"
          "Press 3 to restock the machine.\n"
          "Press q to shutdown the machine.")

if __name__ == '__main__':
  a = Simulator(1, 10, 10, 10)
  a.console()