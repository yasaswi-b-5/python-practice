
'''1. Write a Python program to create a class Student that stores the student's name and age. Create an object of the class and display the student's details.
Input:
John
21
Output:
Name: John
Age: 21'''
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
s=Student("John",21)
s.display()
'''
'''2.Write a Python program to create a class Rectangle that stores the length and breadth. Create an object and calculate the area of the rectangle.
Input:
5
8
Output:
Area: 40

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def display(self):
        print('area:',self.length*self.breadth)
        
s=Rectangle(5,8)
s.display()'''

'''3.Write a Python program to create a class Calculator that stores two numbers. Create an object and find their sum.
Input:
10
20
Output:
Sum: 30
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print('sum:',self.a+self.b)
       
s=Calculator(10,20)
s.display()'''


'''4.Write a Python program to create a class Employee that stores the employee's name and salary. Create an object and display the employee details.
Input:
Rahul
45000
Output:
Employee Name: Rahul
Salary: 45000
class Employee:
    def __init__(self,employee,salary):
        self.employee=employee
        self.salary=salary
    def display(self):
        print('Employee:',self.employee)
        print('Salary:',self.salary)
s=Employee("Rahul",45000)
s.display()'''

'''5.Write a Python program to filter all strings whose length is greater than 5 using the filter() function.
Input:
apple mango cat elephant dog python
Output:
elephant python'''
class FilterStrings:
    def display(self):
        text = input("Enter the strings: ")
        words = text.split()

        result = filter(lambda x: len(x) > 5, words)

        for i in result:
            print(i, end=" ")

obj = FilterStrings()
obj.display()
