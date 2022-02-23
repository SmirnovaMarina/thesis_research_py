import numpy as np

class CoffeMachine:

  # Initializing the products
  def __init__(self):
    self.balance = 0
    self.coffee = 20
    self.milk = 20
    self.sugar = 20
    self.cups = 2

  # Turn on/off
  def power_machine(self, value):
    if value == 0:
      print('Coffee machine turned off')
    else:
      print('Coffee machine turned on')

  # Display the amount of products left 
  def display_products(self):
    print('The coffee machine currently has:')
    print('-'*35)
    print('Coffee: ', self.coffee, '%')
    print('Milk: ', self.milk, '%')
    print('Sugar: ', self.sugar, '%')
    print('Cups: ', self.cups)

  # Refresh the supplies
  def refresh(self):
    self.coffee = 100
    self.milk = 100
    self.sugar = 100
    self.cups = 10

  # Show all the services
  def display_services(self):
    print('What we have:')
    print('-'*35)
    print('1. Cappucino with sugar')
    print('2. Cappucino without sugar')

  # Receive money
  def receive_money(self, value):
    self.balance+=value
    print('\nPayment successful. Here is your cup of cappucino!')

  # Make 1 cup of cappucino
  def make_cappucino(self, sugar_bool):
    if sugar_bool:
      print('A cup of cappucino with sugar is 150rubles')
      money = input('Enter the value in order to proceed to payment>>>\n')
      value = int(money)

      if value == 150:
        self.receive_money(value)
        self.coffee-=10
        self.milk-=10
        self.sugar-=10
        self.cups-=1
      else:
        print('Payment declined :( Try again')

    else:
      print('A cup of cappucino without sugar is 100rubles')
      money = input('Enter the value in order to proceed to payment>>>\n')
      value = int(money)

      if value == 100:
        self.receive_money(value)
        self.coffee-=10
        self.milk-=10
        self.cups-=1
      else:
        print('Payment declined :( Try again')

# Instantiate our coffee machine
coffee_machine = CoffeMachine()