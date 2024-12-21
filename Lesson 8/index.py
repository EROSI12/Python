
def calculate_area(radius):
    return 3.14 * radius * radius

def calculate_circumference(radius):
    return 2 * 3.14 * radius


radius = 5
print("Area:", calculate_area(radius))
print("Circumference:", calculate_circumference(radius))



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):

        return self.length * self.width

    def calculate_circumference(self):

        return 2 * (self.length + self.width)


my_rectangle = Rectangle(5, 3)

print(f"Area of Rectangle: {my_rectangle.calculate_area()}")  # Output: 15
print(f"Circumference of Rectangle: {my_rectangle.calculate_circumference()}")  # Output: 16

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculate_age_in_months(self):

        return self.age * 12

    def years_until_retirement(self):

        retirement_age = 65
        if self.age >= retirement_age:
            return 0
        else:
            return retirement_age - self.age


person = Person("Ronaldo", 40)


print(f"{person.name}'s age in months: {person.calculate_age_in_months()} months")
print(f"Years until {person.name} can retire: {person.years_until_retirement()} years")
