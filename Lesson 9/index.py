
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # Overriding speak method for Cat
    def speak(self):
        return f"{self.name} says Meow!"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the Animal class
        self.breed = breed


    def speak(self):
        return f"{self.name} says Woof!"

cat = Cat("Whiskers", "Siamese")
dog = Dog("Buddy", "Golden Retriever")


print(cat.speak())  # Output: Whiskers says Meow!
print(dog.speak())  # Output: Buddy says Woof!


# Base Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"Vehicle Debug: Creating {self.year} {self.make} {self.model}")  # Debugging creation

    def start(self):
        print(f"Vehicle Debug: Starting the {self.year} {self.make} {self.model}")  # Debugging start
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"Vehicle Debug: Stopping the {self.year} {self.make} {self.model}")  # Debugging stop
        print(f"The {self.year} {self.make} {self.model} is stopping.")


# Derived Class 1 - Single Inheritance
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
        print(f"Car Debug: Adding {self.doors} doors to the {self.year} {self.make} {self.model}")  # Debugging doors

    def start(self):
        print(
            f"Car Debug: Starting the car {self.year} {self.make} {self.model} with {self.doors} doors")  # Debugging start method
        print(f"The {self.year} {self.make} {self.model} car with {self.doors} doors is starting.")

    def display_info(self):
        print(
            f"Car Debug: Displaying info for {self.year} {self.make} {self.model} with {self.doors} doors")  # Debugging info
        print(f"{self.year} {self.make} {self.model} with {self.doors} doors.")


# Create a BMW instance to debug
bmw_car = Car("BMW", "X5", 2023, 4)

# Debugging: Call start method and display info
bmw_car.start()
bmw_car.display_info()
bmw_car.stop()

# Define a string
my_string = "Hello, World!"

# Calculate the length of the string using len()
string_length = len(my_string)

# Output the length of the string
print(f"The length of the string is: {string_length}")

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the length of the list using len()
list_length = len(numbers)

# Output the length of the list
print(f"The length of the list is: {list_length}")

