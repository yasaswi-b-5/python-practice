#3. Write a Python program using a while loop to check whether a given number is a prime number or not.
#Input:7
#Output:Prime Number
#Input:8
#Output:Not Prime Number
#Explanation:
#A prime number is divisible only by 1 and itself.'''
'''num=int(input('enter the num:'))
if num%2!=0 and num%1==0:
        print('prime')
else:
        print('not prime')'''

#2. Write a Python program using a while loop to find the Greatest Common Divisor of two numbers.
#Input:24 36
#Output:GCD = 12
#Explanation:
#12 is the largest number that divides both 24 and 36 exactly.
'''a = int(input('enter a:',))
b = int(input('enter b:',))
while b:
    a, b = b, a % b
print("GCD =", a)'''

#1. Write a Python program using a while loop to calculate the sum of the first N natural numbers and determine whether the sum is even or not.
#Input:10
#Output:
#Sum = 55
#Not Even
#Explanation:
#The sum of the first 10 natural numbers is 55. Since 55 is not divisible by 2, the sum is not even.'''
'''n=1
num=int(input('enter the num:',))
sum=0
while n<=num:
    sum=sum+n
    n=n+1
print(sum)
if sum%2==0:
     print('even')
else:
     print('not even')'''

#4. Write a Python program using a while loop to print all prime numbers from 1 to 100.
#Output:
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
#Explanation:
#Print all numbers between 1 and 100 that have exactly two factors.




#5. Write a Python program using a while loop to check whether a given number is a palindrome or not.
#Input:121
#Output:Palindrome Number
#Input:123
#Output:Not a Palindrome Number
#Explanation:
#A palindrome number remains the same when reversed.
'''num=int(input('enter the num:',))
rev=0
org_num=num
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
if rev==org_num:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')'''

#6. Write a Python program using a while loop to reverse a given number.
#Input:1234
#Output:4321
#Explanation:
#Extract each digit and construct the reversed number.
'''num=int(input('enter the num:',))
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
print(rev)'''

#7. Write a Python program using a while loop to count the number of digits in a given number.
#Input:56789
#Output:5
#Explanation:
#The number contains 5 digits.
'''num=int(input('enter the num:',))
count=0
while num>0:
    d=num%10
    count=count+1
    num=num//10
print(count)'''

#8. Write a Python program using a while loop to find the sum of digits of a given number.
#Input:345
#Output:12
#Explanation:
#3 + 4 + 5 = 12
'''num=int(input('enter the num:',))
sum=0
if num%10==0:
    sum=sum+num
print(sum)'''

#9.Write a Python program using a while loop to calculate the factorial of a given number.
#Input:5
#Output:120

#Explanation:
#5 × 4 × 3 × 2 × 1 = 120
'''num=int(input('enter the num:',))
n=1
fac=1
while n<=num:#5<=5
    fac=fac*n#24*5=120
    n=n+1#2+1
print(fac)'''

