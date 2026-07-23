#1.A movie theater has 20 seats. Seats with numbers divisible by 5 are reserved. Write a program to display only the available seat
'''num=1
while num<=20:
    if num%5!=0:
        print(num)
    num=num+1 '''
#2.A company issues employee IDs from 1001 to 1020. Write a program to count how many employee IDs are even?
'''count=0
id=1001
while id<=1020:
    if id%2==0:
        count=count+1
    id=id+1
print(count)'''
#3.A game contains 15 levels. Bonus rewards are given for levels divisible by 3. Write a program to display all bonus levels?
'''level=1
bonus=0
while level<=15:
    if level%3==0:
        print('level:',level)
        bonus=bonus+1
    level=level+1'''
#4.A library contains books numbered from 1 to 50. Write a program to count how many book numbers are multiples of 7?
'''book=1
count=0
while book<=50:
    if book%7==0:
        count=count+1
    book=book+1
print(count)'''
#5.Write a program to find the first number greater than 100 that is divisible by both 7 and 9 using a while loop?
'''num=100

while num>=100:
    if num%9==0 and num%7==0:
        print(num)
        break
    num=num+1'''
#6.Write a program to print all numbers from 1 to n whose square is less than 50?
'''num=1
n=int(input('enter the n:'))
while num<=n:
    if  num**2<n:
        print(num)
    num=num+1'''
#7.Write a program to count how many numbers between m and n are perfect squares.
'''m=int(input('enter the m:',))
n=int(input('enter the n:',))
count=0
num=1

while num*num<=n:
   sq=num*num
   if sq>=m: 
        
         count=count+1
   num=num+1
          
print(count)'''
            

      





