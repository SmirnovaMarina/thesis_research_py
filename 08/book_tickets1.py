from seating import Seating

def book(name, surname, number, seatings):
    
    seatings[int(number-1)].book(name, surname)