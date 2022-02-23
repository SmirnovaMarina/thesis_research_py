time_slots = ["10:00", "15:00", "20:00"]
seats = {}


def time_choosing():
    print("Chose options time to go to cinema or exit if you completed")
    print("0) exit")
    for i in range(len(time_slots)):
        print(f"{i + 1}) {time_slots[i]}")

    inp = input()

    while True:
        try:
            if inp == "0":
                return "exit"
            return time_slots[int(inp)]
        except:
            print("Incorrect input, try again")
            print("Chose options time to go to cinema or exit if you completed")
            print("0) exit")
            for i in range(len(time_slots)):
                print(f"{i + 1}) {time_slots[i]}")

            inp = input()


class seatInformation:
    currentState = "_"
    cost = 300
    name = ""
    surname = ""

    def __init__(self, *args):
        if len(args) == 0:
            pass
        elif len(args) == 2:
            self.name = args[0]
            self.surname = args[1]
        else:
            self.cost = int(args[0])

    def getState(self):
        return self.currentState


def choose_sit(seat_arr):

    while True:
        try:
            print("Choose available seat:")
            display_sits(seat_arr)

            seatPos = input()
            seat = seat_arr[int(seatPos) - 1]
            if seat.currentState == "x":
                print("This seat is occupied")
            else:
                seat.currentState = "x"
                print("Enter your name")
                name = input()
                seat.name = name
                print("Enter your surname")
                surname = input()
                seat.surname = surname
                print(f"This will cost you {seat.cost} bucks $$$")
                break
        except:
            print("Try again")


def display_sits(seat_arr):
    print("\t".join([seat.getState() for seat in seat_arr]))
    print("\t".join([str(i + 1) for i in range(len(seat_arr))]))


print("This is admin panel. Set default cost for all seats:")
def_cost = int(input())

for i in time_slots:
    seats[i] = [seatInformation(def_cost) for i in range(10)]

while True:
    slot = time_choosing()
    if slot == "exit":
        break

    choose_sit(seats[slot])
