'''
– Have a console menu with options: book tickets, display the current state of the
seating arrangement for each time slot, and exit.
– Display the seating arrangement (for the chosen time slot) by printing it to the
console: show the number of the seat and mark free seats with "_", occupied seats with "x". 
– Receive an order for booking a ticket: ask for customer's name, surname, and save the information about the booking. 
– Display the ticket price.
– Set the ticket price. 

'''

from seating import Seating
from book_tickets import book as book
from display_arrangement import display_arrangement as display_arrangement

print("Welcome to the SEATS BOOKING SIMULATOR.")
print("Please, enter the number of the action to perform:")
print("1 - book tickets")
print("2 - display the current seating arrangement")
print("3 - exit")

seatings_1000 = []
for i in range(10):
    seatings_1000.append(Seating(i+1))
    
seatings_1500 = []
for i in range(10):
    seatings_1500.append(Seating(i+1))
    
seatings_2000 = []
for i in range(10):
    seatings_2000.append(Seating(i+1))
    
seatings = {"10:00": seatings_1000, "15:00": seatings_1500, "20:00": seatings_2000}

while True:
    action = input()
    
    if(action == '1'):
        print("Please, enter the time in format HH:MM")
        time = input()
            
        if time not in seatings.keys():
            print("There is no such timeslot. Please try again.")
            continue
        
        print("Please, enter your name:")
        name = input()
        print("Please, enter your surname:")
        surname = input()
        print("Please, enter the seating number:")
        number = input()
        
        book(name, surname, number, seatings[time])
        
    elif(action == '2'):
        print("Please, enter the time in format HH:MM")
        time = input()
            
        if time not in seatings.keys():
            print("There is no such timeslot. Please try again.")
            continue
        
        display_arrangement(seatings[time], time)
        
    elif(action == '3'):
        break