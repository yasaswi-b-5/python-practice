'''8.Write a python programme to Create a Number class and overload the + operator to add two Number objects.
 Sample input First number: 10 Second number: 20 Expected output Sum: 30'''
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


n1 = Number(10)
n2 = Number(20)

result = n1 + n2

print("Sum:", result.value)



'''9.Write a python programme to Create a Student class with a marks attribute. 
Overload == to check whether two students have the same marks. Sample input Student 1 marks: 85 Student 2 marks: 85 
Expected output Both students have equal marks'''
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks


s1 = Student(85)
s2 = Student(85)

if s1 == s2:
    print("Both students have equal marks")
else:
    print("Students have different marks")



'''10.Write a python programme to Create a Shape class with an area() method. Override it in Rectangle and Circle. 
Sample input Rectangle length: 5 Rectangle width: 4 Circle radius: 3 
Expected output Rectangle area: 20 Circle area: 28.27'''
import math

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


rectangle = Rectangle(5, 4)
circle = Circle(3)

print("Rectangle area:", rectangle.area())
print("Circle area:", round(circle.area(), 2))



'''11.Write a python programme to Create Dog, Cat, and Cow classes, each with a sound() method. 
Write one function that accepts any of these objects and calls sound().
 Expected output Bark Meow Moo'''
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)
make_sound(cat)
make_sound(cow)