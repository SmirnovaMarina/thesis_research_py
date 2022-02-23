"""##COFFEE MACHINE SIMULATOR

In this task, you will work on programming a coffee machine simulator. The machine works with typical products: coffee, milk, sugar, and plastic cups; if it runs out of something, it shows a notification. For simplicity, there is only one type of coffee to serve – cappuccino. Since nothing’s for free, it also collects the money. Sugar is an optional ingredient. The requirements are described below. 

The machine should:
*   Have "turn on" and "turn off" features. 
*   Have a console menu with services that the machine provides. 
*   Assume that the machine needs 1 portion of coffee + 1 portion of milk for cappuccino + 1 plastic cup. 
*   Display the amount of supplies (coffee, milk, sugar, and plastic cups) left. 
*   Show notification if the machine runs out of something. 
*   Have "refresh" feature for the supplies (coffee, milk, sugar, and plastic cups). 
*   Receive orders for coffee: collect money and serve the coffee (you can assign any prices). 
"""

class coffee_machine():
  def __init__(self):
    self.state = False
    self.portions = 15
    self.sugar = 15
    self.price = 20
    self.total = 0
  
  def check_state(self):
    if self.state:
      print("Machine is on")
    else:
      print("Machine is off")
  
  def refresh_supplies(self):
    self.portions = 15
    self.sugar = 15
  
  def display_amounts(self):
    print("Sugar porpotions left: ", self.sugar)
    print("coffee, milk, and plastic cups left: ",self.portions)
  
  def disp_runs_out():
    print("Machine is out of stuff")
  
  def order_coffee(self, amt, sugar=0):
    if self.portions-amt>0:
      self.portions -= amt
      self.total += self.price*amt
      print("Coffee provided")
      print("Balance: ", self.total)
      print("propotions left: ", self.portions)
    else:
      print("not enough material")
      self.disp_runs_out()
    if self.sugar-sugar>0:
      self.sugar -= sugar

  def console(self):
    print("Enter the amount of coffee cups required:")
    cups = int(input())
    print("Sugar required for how many cups?")
    sugar = int(input())
    self.order_coffee(amt=cups, sugar=sugar)

obj = coffee_machine()

obj.console()

