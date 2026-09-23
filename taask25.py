'''1. Three departments have access to different systems:
hr = {"Amit", "Priya", "Rahul", "Sneha"}
finance = {"Rahul", "Kiran", "Priya", "Vijay"}
it = {"Sneha", "Rahul", "Kiran", "Arjun"}
Find:
1.	Employees who have access to all three departments 
2.	Employees who have access to exactly two departments 
3.	Employees who have access to only one department 
4.	All unique employees 
Expected Output:
All three: {'Rahul'}

Exactly two: {'Priya', 'Sneha', 'Kiran'}

Only one: {'Amit', 'Vijay', 'Arjun'}

All employees: {'Amit', 'Priya', 'Rahul', 'Sneha', 'Kiran', 'Vijay', 'Arjun'}'''

hr = {"Amit", "Priya", "Rahul", "Sneha"}
finance = {"Rahul", "Kiran", "Priya", "Vijay"}
it = {"Sneha", "Rahul", "Kiran", "Arjun"}
Three=hr&finance&it
print("All three:",Three)

two=((hr & finance)|(finance & it)|(it & hr))-(hr & it & finance)
print("exactly two",two)

hr_only=hr-finance-it
it_only=it-hr-finance
finance_only=finance-hr-it
one=hr_only|it_only|finance_only
print("onlyone",one)

all_emp=hr|it|finance
print("All employees:",all_emp)
#===========================================================================================================================================
'''3. Invert a Dictionary
Given:
data = {
    "Amit": "Python",
    "Priya": "Java",
    "Rahul": "Python",
    "Sneha": "C++",
    "Kiran": "Java"
}
Create a dictionary where the language becomes the key and the students become a list of values.
Expected Output:
{
    'Python': ['Amit', 'Rahul'],
    'Java': ['Priya', 'Kiran'],
    'C++': ['Sneha']
}'''


data = {
    "Amit": "Python",
    "Priya": "Java",
    "Rahul": "Python",
    "Sneha": "C++",
    "Kiran": "Java"
}
dic={}
for key,value in data.items():
    if value not in dic.keys():
        dic[value]=[]
    dic[value].append(key)    
print(dic)

#======================================================================================================================================
'''
2. Remove Elements Based on Position
Given:
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
Create a new list containing:
•	Elements at even indexes 
•	Elements at odd indexes 
•	Reverse of the even-index elements 
Expected Output:
Even indexes: [11, 33, 55, 77, 99]
Odd indexes: [22, 44, 66, 88, 100]
Reversed even indexes: [99, 77, 55, 33, 11]'''

data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
print("even_index:",data[0::2])
print("odd_index:",data[1::2])
print("reverse even index:",data[0::2][::-1])
