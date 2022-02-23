from time import sleep

COFFEE_COST = 5

def imitate_loading(time = 3):
    for i in range(time):
        print(".", end='')
        sleep(0.5)
    print()

class coffee_machine:

    maxNmbOfCoffee = 5
    maxNmbOfMilk = 10
    maxNmbOfSugar = 25
    maxNmbOfCups = 15
    # I wanted to implement something like code-lock, but it's not enough time((
    machineCode = 1234

    def __init__(self):
        self.nmbOfCoffee = 0
        self.nmbOfMilk = 0
        self.nmbOfSugar = 0
        self.nmbOfCups = 0
        self.moneyCollected = 0

        self.isTurnedOn = False

    def press_on_button(self):
        imitate_loading()
        self.isTurnedOn = not self.isTurnedOn
        print("Mode changed")

    def is_runs_out_of_ingridients(self):
        return self.nmbOfCoffee == 0 or self.nmbOfCups == 0 or self.nmbOfMilk == 0 or self.nmbOfSugar == 0

    def get_coffee(self):
        imitate_loading()
        if not self.isTurnedOn:
            print("Ooops, something is not working. Probably you should turn on the machine...")
        else:
            if self.nmbOfCoffee == 0 or self.nmbOfCups == 0 or self.nmbOfMilk == 0:
                print("Ooops, there is not enough ingridients for making you coffee, sorry...")
            else:
                self.nmbOfCoffee -= 1
                self.nmbOfMilk -= 1
                self.nmbOfCups -= 1

                while True:
                    try:
                        print("Enter amount of sugar you want using number from 0 to 5:")
                        sugAmount = int(input())
                        imitate_loading()
                        if 0 <= sugAmount <= 5:
                            if self.nmbOfSugar >= sugAmount:
                                self.nmbOfSugar -= sugAmount
                                self.moneyCollected += COFFEE_COST
                                break
                            else:
                                print(f"Sorry, there is not enough sugar in the machine. Current amount is {self.nmbOfSugar}. Try again")
                    except:
                        print("Try again...")

                print("Thank you for buying coffee. See you next time!!!")

    def display_amounts(self):
        imitate_loading()
        if not self.isTurnedOn:
            print("Ooops, something is not working. Probably you should turn on the machine...")
        else:
            print("Coffee:", self.nmbOfCoffee)
            print("Milk:", self.nmbOfMilk)
            print("Sugar:", self.nmbOfSugar)
            print("Cups:", self.nmbOfCups)
            print("Collected money:", self.moneyCollected)

    def refresh(self):
        imitate_loading()
        self.nmbOfCoffee = self.maxNmbOfCoffee
        self.nmbOfMilk = self.maxNmbOfMilk
        self.nmbOfSugar = self.maxNmbOfSugar
        self.nmbOfCups = self.maxNmbOfCups

machine = coffee_machine()

while True:
    if machine.isTurnedOn:
        if machine.is_runs_out_of_ingridients():
            print("Machine is running out of ingridients. It should be refreshed")

    print("Which operation you want to proceed?")
    print("0) Exit")
    print("1) Turn on the machine")
    print("2) Get a cup of coffee")
    print("3) Display amount of ingridients")
    print("4) Refresh")

    case = input()

    if case == "0":
        break
    elif case == "1":
        machine.press_on_button()
    elif case == "2":
        machine.get_coffee()
    elif case == "3":
        machine.display_amounts()
    elif case == "4":
        machine.refresh()
    else:
        print("Try again...")