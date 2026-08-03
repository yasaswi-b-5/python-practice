1.Exam Score Calculation
A student receives marks for 5 subjects one by one.
Write a Python program using a while loop to calculate the total marks and average.

Input:80 75 90 85 70
Output:
Total = 400
Average = 80
total=0
n=5
i=1
while i<=5 :
  marks=int(input("enter the marks:"))
  if marks<=100:
    
    
  
    total=total+marks          
    i=i+1       
avg=total//n   
print("Total:",total)
print("Average:",avg)


2.Grocery Shopping
A customer keeps adding item prices until the total bill exceeds ₹1000.
Write a Python program using a while loop to calculate the final bill and the number of items purchased.

Sample Input:
250
300
200
400

Output:
Total Bill = 1150
Items Purchased = 4
sum=0
count=0

while sum<1000:
    n=int(input("enter the num:"))
    sum=sum+n
    count=count+1
    
print("Total Bill=",sum)
print("Items Purchased=",count)

3.Write a Python program using a while loop to count how many numbers must be added starting from 1 until the sum becomes greater than N?
Input:20
Output:6
Explanation:1 + 2 + 3 + 4 + 5 + 6 = 21
num=int(input('enter the num:',))
sum=0
n=1
count=0
while num>0:
 
  sum=sum+n
  count=count+1
  if sum>=num:
      
      
      break
  n=n+1
  
print(count)
4.Write a Python program using a while loop to check whether a given number is a palindrome or not. If the number is a palindrome, determine whether it is even or odd?

Input:1221
Output:
Palindrome Number
Even
num=int(input('enter the num:',))
pal=0
bkp=num
while num>0:
    d=num%10
    pal=pal*10+d   
    num=num//10

if pal==bkp:
    print('palindrome')
    if pal%2==0:
       print('even')
    else:
       print('odd')  
else:
    print('not a palindrome')






5.Write a Python program using a while loop to find the smallest number greater than N whose sum of digits is equal to 10?

Input:25
Output:28

Explanation:
The numbers greater than 25 are:
26 → 2 + 6 = 8
27 → 2 + 7 = 9
28 → 2 + 8 = 10 
Therefore, 28 is the smallest number greater than 25 whose digit sum is 10.
for i
num=int(input('enter the num:',))
i=num+1

while True:
    bpk=i
    sum=0 
    while bpk>0:
        d=bpk%10
        sum=sum+d
        bpk=bpk//10
    
    if sum>=10:
        print(i)
        break
    i=i+1









