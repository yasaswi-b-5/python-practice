#1.Write a program to display the floor numbers in a building using a while loop?

#Output:
#Floor 1
#Floor 2
#Floor 3
#Floor 4
#Floor 5
#Explanation:
#Assume a building has 5 floors and display each floor number.
'''num=int(input('enter the number',))
i=1
while i<=num:      


 print('floor',i)
 i=i+1'''
#2.Write a program to display the days remaining for an event using a while loop?

#Input:
#5

#Output:
#5 Days Left
#4 Days Left
#3 Days Left
#2 Days Left
#1 Day Left

#Explanation:
#Display the countdown until the event starts.
num=int(input('enter the number',))
i=5
while i>=num:      


 print(i,'Days Left')
 i=i-1

#3.Write a program to display the first 10 customer token numbers in a bank using a while loop?

#Output:
#Token 1
#Token 2
#Token 3
#...
#Token 10

#Explanation:
#Generate token numbers for customers.
'''num=int(input('enter the number',))
i=1
while i<=num:      


 print('Token',i)
 i=i+1'''


#4.Write a program to display bus stop numbers from 1 to n using a while loop?

#Input:
#6

#Output:
#Bus Stop 1
#Bus Stop 2
#Bus Stop 3
#Bus Stop 4
#Bus Stop 5
#Bus Stop 6

#Explanation:
#Display all bus stops on a route.
'''num=int(input('enter the number',))
i=1
while i<=num:      


 print('Bus Stop',i)
 i=i+1'''
 

#5.Write a program to display the first n levels of a game using a while loop?

#Input:
#5

#Output:
#Level 1
#Level 2
#Level 3
#Level 4
#Level 5

#Explanation:
#Display all game levels from 1 to n.
'''num=int(input('enter the number',))
i=1
while i<=num:      


 print('Level',i)
 i=i+1'''
#6.Write a program to find the sum of all numbers from 1 to n that are divisible by 3 using a while loop?

#Input:
#10

#Output:
#18

#Explanation:
#3 + 6 + 9 = 18
'''num=int(input('enter the number',))
i=1
sum=0
while i<=num:      
 if i%3==0:
     sum=sum+i
 
 
 i=i+1
print(sum) '''
 

#7.Write a program to count how many numbers between 1 and n are divisible by 5 using a while loop?

#Input:
#25

#Output:
#5

#Explanation:
#The numbers are 5, 10, 15, 20, and 25.
'''i=1
num=int(input('enter the number',))

count=0
while i<=num:      
 if i%5==0:
     count=count+1
 
 
 i=i+1
print(count)'''

#8.Write a program to print all numbers between 1 and n that are divisible by both 2 and 3 using a while loop?

#Input:
#20

#Output:
#6 12 18

#Explanation:
#These numbers are divisible by both 2 and 3.
'''i=1
num=int(input('enter the number',))


while i<=num:      
 if i%6==0:
     print(i)
 
 
 i=i+1'''


#9.Write a program to find the sum of squares of numbers from 1 to n using a while loop?

#Input:
#4

#Output:
#30

#Explanation:
#1² + 2² + 3² + 4² = 30
'''i=1
num=int(input('enter the number',))
sum=0

while i<=num:      
      sq=i**2
      sum=sum+sq
      i=i+1
print(sum)'''
 
 

 

#10.Write a program to find the sum of cubes of numbers from 1 to n using a while loop?

#Input:
#3

#Output:
#36

#Explanation:
#1³ + 2³ + 3³ = 36
'''i=1
num=int(input('enter the number',))
sum=0

while i<=num:      
      sq=i**3
      sum=sum+sq
      i=i+1
print(sum)'''
 
