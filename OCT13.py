'''1.Create an Employee class with name and salary. 
Create a Manager class that adds department. 
Sample Input Name: Priya Salary: 50000 Department: HR 
Expected Output Name: Priya Salary: 50000 Department: HR'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

m = Manager("Priya", 50000, "HR")
m.display()



'''2.Create an Animal class with an eat() method, a Dog class with a bark() method, 
and a Puppy class with a play() method. Sample Input Create object: Puppy
 Expected Output Animal can eat Dog can bark Puppy can play '''
class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

class Puppy(Dog):
    def play(self):
        print("Puppy can play")

p = Puppy()
p.eat()
p.bark()
p.play()



'''3.Create an Addition class and a Multiplication class. 
Create a Calculator class that inherits from both. 
Sample Input First number: 10 Second number: 5 
Expected Output Addition: 15 Multiplication: 50'''
class Addition:
    def add(self, a, b):
        print("Addition:", a + b)

class Multiplication:
    def multiply(self, a, b):
        print("Multiplication:", a * b)

class Calculator(Addition, Multiplication):
    pass

c = Calculator()
c.add(10, 5)
c.multiply(10, 5)



'''4.Create a Shape parent class. Create Circle and Rectangle child classes that 
calculate their respective areas. 
Sample Input Circle radius: 7 Rectangle length: 5 Rectangle width: 4
Expected Output Circle area: 153.94 Rectangle area: 20'''
class Shape:
    pass

class Circle(Shape):
    def area(self, radius):
        print("Circle area:", round(3.14 * radius * radius, 2))

class Rectangle(Shape):
    def area(self, length, width):
        print("Rectangle area:", length * width)

c = Circle()
c.area(7)

r = Rectangle()
r.area(5, 4)



'''5.Create a Person class. Let Student and Employee inherit from Person,
 then create WorkingStudent that inherits from both Student and Employee. 
 Sample Input Name: Kiran Age: 22 Course: Python Company: ABC 
 Expected Output Name: Kiran Age: 22 Course: Python C'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

class WorkingStudent(Student, Employee):
    def __init__(self, name, age, course, company):
        Person.__init__(self, name, age)
        self.course = course
        self.company = company

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Company:", self.company)

w = WorkingStudent("Kiran", 22, "Python", "ABC")
w.display()

 

'''6.Create a Person class that accepts a name in its constructor. 
Create a Student class that uses super() and adds a roll number.
 Sample Input Name: Ravi Roll number: 101 Expected Output Name: Ravi Roll number: 101'''
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number

    def display(self):   
        print("Name:", self.name)
        print("Roll number:", self.roll_number)

s = Student("Ravi", 101)
s.display()

