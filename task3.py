#1. Write a program to print all numbers from 1 to n that leave a remainder of 1 when divided by 3.
'''n=int(input('enter n:'))
number=1
while number<n:
    if number%3==1:
        print(number)
    number=number+1'''
#2. Write a program to count how many numbers between 1 and n are greater than 20.
'''count=0
n=int(input('enter n:',))
number=1
while number<=n:
                if number>20:
                    count=count+number
                    print(number)
                number+=1
print(count)'''
#3. Write a program to print all numbers between 1 and n except multiples of 5.
'''n=int(input('enter the number:'))
num=1
while num<=n:
    if num<=n and num%5!=0:
        print(num)
     
    num=num+1'''
#4. Write a program to find the sum of all numbers between m and n.
'''sum=0
m=int(input('enter m:',))
n=int(input('enter n:',))
while m<=n:
    sum=sum+m
    m=m+1

print(sum)'''
#5.Write a program to count the number of odd numbers between m and n.
count=0
'''n=int(input('enter the n:'))#8
m=int(input('enter the m:'))#2
while m<=n:#35<=8-T
    if m%2==1:#5%2==1-F
        count=count+1#3
        
    m+=1#5  
print(count)'''
#6.Write a program to print all multiples of a given number that are less than n.
'''NUM=1
table=int(input("enter the table u want:",))#6
n=int(input('enter n'))#4
while NUM<=n:#1<=4
    
      print(table*NUM)#6*1
      NUM=NUM+1'''
#7.Write a program to find the sum of numbers that are divisible by 4 between 1 and n.
'''num=1
sum=0
n=int(input('enter the n:',))
while num<=n:
    if num%4==0:
      sum=sum+num
    num=num+1
print(sum)'''
#8.Write a program to print numbers from n to 1 by decreasing 2 each time.
'''n=int(input ('enter the n:'))
num=1
while n>=num:
      
    print(n)
    n=n-2'''
#9.Write a program to count how many numbers between 1 and n are not divisible by 3.
'''count=0
num=1
n=int(input('enter the n:'))
while num<=n:
    if num%3!=0:
        count=count+1
    num=num+1
print(count) '''   

      

