#1.Write a Python program using a while loop to find the smallest number greater than n whose last digit is 7?
#Input:25
#Output:27
#Explanation:
#Continue checking numbers until a number ending with 7 is found.'''
'''
num=int(input('enter the num:',))
while num>0:
    r=num%10
    if r==7:
      print(num)
      break
    num=num+1'''

#2.Write a Python program using a while loop to find the sum of all numbers between 1 and n whose last digit is an odd number.
#Input:15
#Output:64
#Explanation:
#1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64'''
'''
num=int(input('enter the num:',))
n=1
while n<=num:
    if n %2!=0:
        print(n)
    n=n+1'''

#3.Write a Python program using a while loop to repeatedly add the digits of a number until a single digit is obtained?
#Input:9875
#Output:2
#Explanation:
#9 + 8 + 7 + 5 = 29
#2 + 9 = 11
#1 + 1 = 2


'''
num=int(input('enter the num:',))
while num>9:
    sum=0
    while num>0:
        last= num%10
        sum=sum+last
        num=num//10
    num=sum
print(num)'''
    
#4.Write a Python program using a while loop to determine how many times a number can be divided by 2 before it becomes odd?
#Input:48
#Output:4
#Explanation:48 → 24 → 12 → 6 → 3
#The number can be divided by 2 four times.

'''
num=int(input('enter the num:',))
count=0
while num%2==0:
    num=num//2
    count=count+1
print(count)  '''  




#5.Write a Python program using a while loop to find the largest digit in a number without converting the number into a string.
#Input:583921
#Output:9
#Explanation:
#Extract each digit and keep track of the maximum dig


num=int(input('enter the num:',))
big=0
while num>0:
    d=num%10
    if d>big:
        big=d
    num=num//10
print(big)     



