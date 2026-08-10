'''
1.Write a Python program to count the number of even and odd elements in a list.
Input:
[10, 15, 20, 25, 30, 35]
Output:
Even Count = 3
Odd Count = 3'''
a=[10,15,20,25,30,35]
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print('even_count=',even_count)
print('odd_count=',odd_count)


'''2.Write a Python program to find the largest element in a list.
Input:
[12, 45, 7, 89, 23]
Output:
89'''
a=[12, 45, 7, 89, 23]
max=a[0]
for i in a:
    if i>max:
        max=i

print(max)




'''3.Write a Python program to count the number of prime numbers in a list.
Input:
[2, 4, 5, 7, 8, 11, 15]
Output:
4'''
a=[2, 4, 5, 7, 8, 11, 15]
d=2
count=0
for i in a:
    if i//2%d!=0:
        count=count+1
d=d+1        
print(count)        
'''4.Write a Python program to find the sum of all elements in a list.
Input:
[10, 20, 30, 40]
Output:
100'''
a=[10,20,30,40]
sum=0
for i in a:
    if i>0:
        sum=sum+i
print(sum)

'''5.Write a Python program to count how many numbers in a list are divisible by 3.
Input:
[3, 5, 6, 9, 10, 12, 15]
Output:
5'''
a=[3,5,6,9,10,12,15]
count=0
for i in a:
    if i%3==0:
        count=count+1
print(count)
        
'''6.Write a Python program to find all palindrome numbers in a list.
Input:
[121, 123, 454, 567, 787]
Output: 121 454 787'''
a=[121, 123, 454, 567, 787]
for i in a:
  rev=0
  bkp=i
  while i>0:
    d=i%10
    rev=rev*10+d
    i=i//10
  if bkp==rev:
      print(bkp,end=" ")











