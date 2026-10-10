#Create a Student class with public attributes name and age. Create an object and access both attributes outside the class.
class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age
student1 = Student("Alice", 20)
print("Name:", student1.name)
print("Age:", student1.age)   



#Create a BankAccount class with a private attribute __balance. Add a method display_balance() to display the balance.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def display_balance(self):
        print("Current Balance:", self.__balance)
account = BankAccount(1000)
account.display_balance() 



#Create a Vehicle class with a protected method _start_engine(). Call it from another method in the same class
class Vehicle:
    def _start_engine(self):  
        print("Engine started!")
    def drive(self):
        print("Starting vehicle...")
        self._start_engine()  
car = Vehicle()
car.drive()



#Create a Student class with private attribute __marks. Add a setter method that accepts marks only between 0 and 100.
class Student:
    def __init__(self):
        self.__marks = 0  
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print(f"Marks updated to: {self.__marks}")
        else:
            print("Invalid input! Marks must be between 0 and 100.")
    def get_marks(self):
        return self.__marks
student = Student()
student.set_marks(85)   
student.set_marks(150)  
