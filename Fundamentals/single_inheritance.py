# Class is always defined with a capital letter

# Parent class
class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    def display(self):
        print('Name:', self.name)
    
    def vehicle_info(self):
        print(f"Color: {self.color}\nPrice: {self.price}")

# Child Class
class Car(Vehicle):
    def __init__(self, name, color, price, model):
        super().__init__(name, color, price)
        self.model = model
    
    # Polymorphism: child class overrides parent method: here it's display() method being overridden
    def display(self):
        print(f"Name: {self.name}\nModel: {self.model}")
    
    def car_info(self):
        print(f"Model: {self.model}\nPrice: {self.price}")

if __name__ == "__main__":
    car = Car("BMW", "Burgundy", "$50000", "X5")
    # car.display()
    # car.car_info()
    # car.vehicle_info()