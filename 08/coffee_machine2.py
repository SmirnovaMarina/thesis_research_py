'''
I tried to implement "do one thing" principle: each method in the class performs
serves for exactly one functionality feature.
Also, I tried to give to each structural unit of the code (class, method, variable)
exactly one sense, so that (in refactoring purposes) extraction of it off the code would result in
extraction of exactly one functional block.

I used a lot of methods to distribute the functionality of the coffee machine between them
and not to overload methods.

I gave meaningful names to the code elements.

I tried to make my programs readable from top to bottom.

I used blank lines to provide the vertical distance and openness.

I think I haven't localised input and output in subroutines, and that harms the code readability and cleanness.

'''

class Coffee_machine:
    def __init__(self):
        self.is_on = False
        
        self.coffee = 15
        self.milk = 15
        self.sugar = 40
        self.cups = 70
        
        self.money = 0
        self.cup_price = 10
        
    def turn_on(self):
        self.is_on = True
        self.on_state()
        
    def on_state(self):
        print("The Coffee Machine is now turned on!")
        self.listen()
        
    def listen(self):
        while True:
            print("To make a cappuccino order - input '1'")
            print("To display the amount of supplies - input '2'")
            print("To add supplies - input '3'")
            print("To turn the coffee machine off - input 'OFF'\n")
            
            self.check_supplies()
            
            input_text = input()
            if input_text == "OFF":
                break
            
            self.process_input(input_text)
        
        self.turn_off()
        
    def check_supplies(self):
        if self.coffee < 5:
            print("Coffee is running out!")
            
        if self.milk < 5:
            print("Milk is running out!")
            
        if self.sugar < 10:
            print("Sugar is running out!")
            
        if self.cups < 5:
            print("Cups are running out!")
        
    def process_input(self, text):
        if text == 'OFF':
            self.turn_off()
            
        elif text == '1':
            self.order()
            
        elif text == '2':
            self.display_supplies()
            
        elif text == '3':
            self.add_supplies()
            
        else:
            print("Unknown command. Please, try again.")
            self.listen()
            
    def order(self):
        self.coffee -= 1
        self.milk -= 1
        self.sugar -= 1
        self.cups -= 1
        
        self.money += self.cup_price
        
        print("Enjoy your tasty cappuccino!\n")
        
    def display_supplies(self):
        print("Coffee: ", self.coffee)
        print("Milk: ", self.milk)
        print("Sugar: ", self.sugar)
        print("Cups: ", self.cups, "\n")
        
    def add_supplies(self):
        print("Input the amount of coffee to add: ")
        self.coffee += int(input())
        print("Input the amount of milk to add: ")
        self.milk += int(input())
        print("Input the amount of sugar to add: ")
        self.sugar += int(input())
        print("Input the amount of cups to add: ")
        self.cups += int(input())
        
    def turn_off(self):
        self.is_on = False
        self.off_state()
        
    def off_state(self):
        while True:
            print("The Coffee Machine is now turned off.")
            print("Please, input ON to turn it on.")
            
            if(input() == "ON"):
                self.turn_on()
                break