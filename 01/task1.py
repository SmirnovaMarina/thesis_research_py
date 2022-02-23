class Person:
    def __init__(self):
        self.name = input("Name: ")
        self.surname = input("Surname: ")

class Counter:
    def __init__(self, times, rooms, roomlimit, price):
        self.times = times.split(",")
        self.seats = [[[None for i in range(roomlimit)] for j in range(rooms)] for k in range(len(self.times))]
        self.price = price
    def show_seating_arrangements(self):
        print("Seating arrangement goes below-")
        for i in range(len(self.times)):
            print("Time:", self.times[i])
            for j in range(len(self.seats[i])):
                print(f"Room {j+1}:")
                print(" ".join(['_' if k is None else "x" for k in self.seats[i][j]]))
    
    def check_price(self):
        print("Current price of the tickets is:", self.price, "Rubles.")

    def set_price(self):
        self.price = int(input("Enter the new ticket price: "))
        print("Price updated to", self.price, "Rubles.")


    def book_ticket(self):
        seats_available = False
        for i in range(len(self.times)):
            free = []
            for j in range(len(self.seats[i])):
                if None in self.seats[i][j]:
                    free.append(j)
                    seats_available = True
            if free:
                print(f"Seat available in {', '.join(['Room ' + str(i+1) for i in free])} at {self.times[i]}" )
        
        if seats_available:
            index = self.times.index(input("Input preferred time: "))
            for i in self.seats[index]:
                for j in range(len(i)):
                    if i[j] is None:
                        i[j] = Person()
                        print("Your seat is booked at Room", self.seats[index].index(i)+1)
                        print("Seat number:", j+1)
                        break
        else:
            print("Sorry no seats available.")

    def main_loop(self):
        print("Welcome to the booking system. Please pick an option from below-")
        while True:
            print("1. Book a ticket\n2. Check seating arrangement\n3. Check ticket price\n4. Set ticket price\n0. Exit")
            entry = int(input("Option: "))
            if entry == 0:
                break
            elif entry == 1:
                self.book_ticket()
            elif entry == 2:
                self.show_seating_arrangements()
            elif entry == 3:
                self.check_price()
            elif entry == 4:
                self.set_price()
            else:
                print("Sorry the option isn't valid. Try again.")


booking = Counter("10:00,15:00,20:00", 1, 10, 250)
print(booking.times)
booking.main_loop()