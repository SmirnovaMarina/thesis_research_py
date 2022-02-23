# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 17:10:02 2022

@author: Dalang, Felix Sihitshuwam
"""

class Ticket:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.seat = None
    self.time = None
    self.cost = None
  
  def set_information(self, time, seat):
    self.seat = seat
    self.time = time
  
  def set_price(self, cost=200):
    self.cost = cost
  
  def __str__(self):
    return "Name: {self.name} {self.surname}\nSeat: {self.seat}\nTime: {self.time}\nCost: Rub.{self.cost}"

class Application:
  def __init__(self):
    """"""
    self.current_time = 0
    self.schedules = {'10:00': 0, '15:00': 0, '20.00': 0}
    self.tickets = []
    
  def check(self, time):
    """Checks Available Seats, Uses FIFO"""
    key = f'{time}:00'
    try:
      val = self.schedules[key]
      taken = 'X '*(val)
      free = '_ ' *(10 - val)
      print("Available Seats (X, taken and _ free seats)")
      print(taken, free)
      if val == 10:
        return 0
      else: 
        return (1, val + 1, key)
    except KeyError:
      return -1
    
  def record(self):
    """
    Method was merged with self.book
    """
  
  def book(self):
    """"""
    while True:
      print("Enter q to go back.")
      time = input("Please Select a time slot (10, 15, 20): ")
      if time == 'q': 
        return
      check = self.check(time)
      if check == -1:
        print("Invalid Input, please input 10, 15 or 20")
      elif check == 0:
        print("You can't book in that time slot. It's filled up.")
      else:
        break
        
    name = input("Please Enter Your Name: ")
    surname = input("Please Enter Your Surname: ")
    
    ticket = Ticket(name, surname)
    ticket.set_information(time, check[1])
    self.schedules[check[2]] = check[1]
    
    self.display_price(ticket)
  
  def console(self):
    out = f"""
    Press 1 to book tickets
    Press 2 to display current state of seating arrangement
    Press q to exit.
    """
    print(out)
  
  def display(self):
    """"""
    keys = self.schedules.keys()
    print('#'*50)
    print("Available Seats (X, taken and _ free seats)")
    for key in keys:
      print(key)
      val = self.schedules[key]
      taken = 'X '*(val)
      free = '_ ' *(10 - val)
      print(taken, free)
    print('#'*50)
      
  
  def display_price(self, ticket):
    ticket.set_price()
    print("Ticket Successfully Booked")
    print(ticket)
  
  

if __name__ == '__main__':
  a = Application()
  while True:
    a.console()
    code = input()
    if code == '1': 
      a.book()
    elif code == '2':
      a.display()
    elif code == 'q':
      print('Exiting')
      break