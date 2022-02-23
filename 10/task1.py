import numpy as np

class Cinema:
  def __init__(self):
    self.seats = []
    self.customers = []

  def display_seats(self):
    print("Sitting arrangement")

    for m in range(10):
      if m % 5 == 0:
        print('\n')
      try:
        if self.seats[m] == 1:
          print('x', end =" ")
      except IndexError:
        print('-', end =" ")
        continue

  def set_ticket_price(self, price):
    self.price = price

  def display_ticket_price(self):
    print(self.price, 'rubles')

  def receive_order(self):
    if len(self.customers) < 10:
      name = input("What's your name?\n")
      surname = input("What's your surname?\n")
      print('Thank you ' + name + ' ' + surname + '!\nNow choose a time from below\n')

      value = input("10:00\n15:00\n20:00\n")
      self.choose_time(name, surname, value)

      number_of_tickets = input('\nHow many tickets would you like? ')

      if int(number_of_tickets)+len(self.customers) > 10:
        print('Sorry we do not have that much seats left, please check the sitting arrangement')
      else:
        print('Your total is: ' , self.price*int(number_of_tickets) , 'rubles. Proceed to pay>>> ')
        [ self.seats.append(1) for n in range(int(number_of_tickets)) ]
        [ self.customers.append(name + ' ' + surname) for n in range(int(number_of_tickets)) ]
    else:
      print('Sorry all seats are booked, please check the sitting arrangement')

  def choose_time(self, name, surname, value):
    while True:
      try:
        time = int(value)
      except ValueError:
        print("Sorry please select from the options above.")
        continue

      if time == 10:
        print(name + ' ' + surname + ' your movie time is 10:00!')
        break
      elif time == 15:
        print(name + ' ' + surname + ' your movie time is 15:00!')
        break
      elif time == 20:
        print(name + ' ' + surname + ' your movie time is 20:00!')
        break
      else:
        print('There are no movies by that time :c')
        value = input("Choose a time from 10:00, 15:00 and 20:00\n")

  def display_customers(self):
    print(self.customers)

cinema_to_book = Cinema()

cinema_to_book.set_ticket_price(450)