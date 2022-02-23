class Seating:
    def __init__(self, number):
        self.number = number
        self.name = ""
        self.surname = ""
        self.is_free = True
        self.price = 100
    
    def book(self, name, surname):
        self.name = name
        self.surname = surname
        self.is_free = False
        
    def free(self):
        self.name = ""
        self.surname = ""
        self.is_free = True
        
    def is_free(self):
        return self.is_free
        
    def set_price(self, new_price):
        self.price = new_price