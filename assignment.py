# Question 1
# Explain how python supports multiple inheritence 
class human:
    def __init__(self):
        print("Human is created")
    def breathe(self):
        print("Human can breathe")
class animal:
    def __init__(self):
        print("Animal is created")
    def breathe(self):
        print("Animal can breathe")
class person(human,animal):
    def __init__(self):
        super().__init__()
        print("Person is created")
    def breathe(self):
        print("Person can breathe")
p = person()
p.breathe()
print("")
# 


# Question 2
# Explain how python demonstrates method overridding
class animal:
    def sound(self):
        print("Animal makes a sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class cat(animal):
    def sound(self):
        print("Cat meows")
d = dog()
d.sound()
print("")

# Question 3
# Implement an abstract class shape with an abstract method area. Create two sub class circle and rectangle that implement the area method
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def area(self5):
        r  = int(input("Enter the radius of the circle: "))
        area = 3.14*r*r
        return area
class rectangle(shape):
    def area(self):
        l = int(input("Enter the length of the rectangle: "))
        b = int(input("Enter the breadth of the rectangle: "))
        area = l*b
        return area
c = circle()
r = rectangle()
print(c.area())
print(r.area())
print("")

# Question 4
# Create a python class Car with attributes brand model year , Create an object of this class and print the attributes
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
Bmw = Car("BMW","X5",2021)
print(Bmw.brand)
print(Bmw.model)
print(Bmw.year)
print("")
