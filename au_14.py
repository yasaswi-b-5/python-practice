''''
1.Method Overriding
Create a parent class Operation with a method calculate().
Create two child classes:

Addition → returns the sum of two numbers.
Multiplication → returns the product of two numbers.

Call calculate() using objects of both child classes.

Sample Input:10 5
Sample Output:
15
50'''
class Operation:
    def calculate(self,a,b):
       return a,b
class Addition:
    def calculate(self,a,b):
       print(a+b)
class Multiplication:
     def calculate(self,a,b):
         print(a*b)
obj = Addition()
obj.calculate(10, 5)

obj = Multiplication()
obj.calculate(10, 5)         

#----------------------------------------------------------------------------------------

'''        
2.Number Pattern
Create a parent class Number that accepts N.
Create a child class Pattern that inherits N and prints:
Sample Input:4
Sample Output:
1
1 2
1 2 3
1 2 3 4'''
class Number:
    def __init__(self, n):
        self.n = n

class Pattern(Number):
    def display(self):
        for i in range(1, self.n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()


obj = Pattern(4)
obj.display()


#--------------------------------------------------------------------------------------------------------------------

'''
3.Encapsulation – Hidden PIN Digit Sum
Create a class SecurePin with a private variable __pin.
Create methods to:
Store a PIN number.
Return the sum of all digits in the PIN without directly accessing the private variable outside the class.
Sample Input:4826
Sample Output:20'''
class SecurePin:
    def __init__(self):
        self.__pin = ""  

    def store_pin(self, pin):
        self.__pin=str(pin)   

    def digit_sum(self):
        total = 0
        for digit in self.__pin:   
            total += int(digit)
        return total


sp = SecurePin()
sp.store_pin(4826)
print(sp.digit_sum())  
#------------------------------------------------------------------------------------------------------------------------------------------
'''4.Inheritance – Digit Difference
Create a parent class Number that stores a number.
Create a child class DigitDifference that inherits the number and finds the difference between the largest digit and smallest digit.
Sample Input:58321
Sample Output:7'''
class Number:
    def __init__(self, num):
        self.num=str(num)

class DigitDifference(Number):   
    def find_difference(self):
        digits=[int(d) for d in self.num]
        return max(digits)-min(digits)


dd = DigitDifference(58321)
print(dd.find_difference()) 
#--------------------------------------------------------------------------------------------------------------------------------------------
'''5.Inheritance – Reverse Triangle Pattern
Create a parent class PatternInput that stores N.
Create a child class ReversePattern that inherits N and prints:

Sample Input:4
Sample Output:
4 4 4 4
3 3 3
2 2
1'''
class PatternInput:
    def __init__(self,n):
        self.n = n

class ReversePattern(PatternInput):   
    def print_pattern(self):
        for i in range(self.n,0,-1): 
            print((str(i)+" ")*i)


rp=ReversePattern(4)
rp.print_pattern()
