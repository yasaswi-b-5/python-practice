'''1.Write a Python program to find the longest word stored as a dictionary value?
Sample Input:{1:'Python',2:'Programming',3:'Code'}
Sample Output:Programming'''
a={1:'Python',2:'Programming',3:'Code'}
t=""
for i in a.values():
    if len(i)>len(t):
        t=i
print(t)    
#==============================================================================================================================================================
'''2.Write a Python program to group student names by their grades?
Sample Input:{'Ram':'A','Sam':'B','John':'A','Tom':'C'}
Sample Output:{'A':['Ram','John'],'B':['Sam'],'C':['Tom']}'''

t={'Ram':'A','Sam':'B','John':'A','Tom':'C'}
d={}
for key,value in t.items():
  if value not in d:
     d[value]=[key]
  else:
     d[value].append(key)
print(d)    
#===========================================================================================================================================================
'''3.Write a Python program to find the product that is out of stock?

Sample Input:{'Pen':20,'Book':0,'Bag':5,'Bottle':0}
Sample Output:
Book
Bottle'''
products={'Pen':20,'Book':0,'Bag':5,'Bottle':0}
for key,value in products.items():
  if value<=0:
   print(key)
#=================================================================================================================================================================
'''4.Task 1: Student Performance Analysis
Create a dictionary where the key is the student name and the value is a list of marks in three subjects?
Perform the following operations:
Calculate the total marks of each student.
Calculate the average marks of each student.
Print the topper's name.
Print the names of students whose average is greater than 75.
Sample Input:
{
'Rahul': [85, 90, 78],
'Priya': [92, 88, 95],
'Arun': [70, 65, 72],
'Neha': [80, 76, 84]
}
Sample Output:
Rahul -> Total: 253, Average: 84.33
Priya -> Total: 275, Average: 91.67
Arun -> Total: 207, Average: 69.00
Neha -> Total: 240, Average: 80.00

Topper: Priya
Students with Average > 75:
Rahul
Priya
Neha
'''

information={
'Rahul': [85, 90, 78],
'Priya': [92, 88, 95],
'Arun': [70, 65, 72],
'Neha': [80, 76, 84]
}
topper=0
topper_name=""

for key,value in information.items():
        sum=0
        
        for marks in value: 
         sum=sum+marks
        avg=sum//len(value)
        print(key,"->","sum:",sum,"avg:",avg)
       
        if sum>topper:
            topper=sum
            topper_name=key
print("Topper:",topper_name)
print("Students with Average > 75:")
for key, value in information.items():
    sum=0
        
    for marks in value: 
         sum=sum+marks
    avg=sum//len(value) 
    if avg>75:
            print(key)
         


