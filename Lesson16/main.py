class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

person1 = Person("John")

person1.greet()

class Animal:
    def __init__(self, name, age, species, breed, color):
        # Constructor to initialize the attributes of the Animal class
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color = color

    def make_sound(self):
        print(f"{self.name} makes a sound!")
    def sleep(self):
        print(f"{self.name} is sleeping.")
    def eat(self):
        print(f"{self.name} is eating.")

animal1 = Animal("Buddy", 5, "Dog", "Golden Retriever", "Golden")

animal1.make_sound()
animal1.sleep()
animal1.eat()
