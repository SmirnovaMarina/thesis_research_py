from typing import Union

class Machine:

    #initialize the coffee machine with some existing items
    def __init__(self, coffee: int, milk: int, sugar: int, cup: int) -> None:
        self.items = {
            "coffee": coffee,
            "milk": milk,
            "sugar": sugar,
            "cup": cup,
        }
        
    
    # add items to the coffee machine
    def refresh(self) -> None:
        for item in self.items.keys():
            count = input(f"Amount of {item}{'s' if item == 'cup' else ' portions'} (Default 0): ")
            if count:
                self.items[item] += int(count)

    # check the status of each items of the machine
    def check_items(self) -> None:
        for item in self.items.keys():
            if self.items[item] > 0:
                print(f"{item.title()}{'s' if item == 'cup' else ' portions'} remaining:", self.items[item])
            else:
                print("The machine is out of", item)

    # check if any of the items is empty
    def is_empty(self) -> Union[str, None]:
        for i in self.items.keys():
            if not self.items[i]:
                return i
    
    # ordering coffee
    def order(self) -> None:
        if self.is_empty():
            print("The machine is out of", self.is_empty())
        else:
            self.check_items()
            sugar_needed = int(input("Amount of sugar needed (0 to 4): "))
            if sugar_needed > self.items['sugar']:
                print("Sorry we do not have the required amount of sugar.")
                return
            self.items['sugar'] -= sugar_needed
            self.items['coffee'] -= 1
            self.items['milk'] -= 1
            self.items['cup'] -= 1
        
            self.collect_bill(250)
            self.check_items()

    # collecting cash
    def collect_bill(self, bill: int) -> int:
        print("Your bill is", bill)
        print("We only support cash payment. Enter the cash amount in the collector.")
        paid = int(input("Amount paid: "))
        while paid < bill:
            print("You still need to pay", bill - paid, "rubles.")
            paid += int(input("Enter the amount: "))
        print("Thanks for paying. Your change is", paid - bill, "rubles.")

    def main_loop(self): # main loop which turns on when the machine is on
        print("Welcome to the coffee machine. Please pick an option from below-")
        while True:
            print("1. Buy a coffeee\n2. Check for items\n3. Refresh machine\n0. Exit")
            entry = int(input("Option: "))
            if entry == 0:
                print("Turning off the machine. Seeya!")
                break
            elif entry == 1:
                self.order()
            elif entry == 2:
                self.check_items()
            elif entry == 3:
                self.refresh()
            else:
                print("Sorry the option isn't valid. Try again.")

# driver program
if __name__ == "__main__":
    machine = Machine(10, 5, 5, 3)
    machine.main_loop()