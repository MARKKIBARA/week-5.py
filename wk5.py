# Base class
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def use_power(self):
        return f"{self.name} uses their superpower: {self.power}!"

# Subclass demonstrating inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, wingspan):
        super().__init__(name, power)
        self.wingspan = wingspan

    def use_power(self):
        return f"{self.name} soars through the skies with a wingspan of {self.wingspan} meters!"

# Another subclass for encapsulation
class TechHero(Superhero):
    def __init__(self, name, power, gadgets):
        super().__init__(name, power)
        self.__gadgets = gadgets  # Encapsulated attribute

    def reveal_gadgets(self):
        return f"{self.name} uses gadgets: {', '.join(self.__gadgets)}"

class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Boat:
    def move(self):
        return "Sailing"
