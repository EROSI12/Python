
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

student1 = Student(name="Drin", age=17)
print("Name:", student1.get_name())
print("Age:", student1.get_age())

student2 = Student(name="Eros", age=18)
print("Name:", student2.get_name())
print("Age:", student2.get_age())


class Animal:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get(self, attribute):
        return getattr(self, attribute, None)

    def set(self, attribute, value):
        setattr(self, attribute, value)

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name=name, breed=breed, age=age)

    def bark(self):
        return f"{self.get('name')} says woof!"