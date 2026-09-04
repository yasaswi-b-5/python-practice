'''5.Write a Python program using a function to generate all possible permutations of a string.

Input: "ABC"
Output:
ABC
ACB
BAC
BCA
CAB
CBA
'''

def permute(s):
    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                if i != j and i != k and j != k:
                    print(s[i] + s[j] + s[k])

permute("ABC")





'''6.Write a Python program that continuously generates the next prime number starting from a given number.
Input:10
Output:
11
13
17
19
23
Generate only the first 5 prime numbers greater than the given input.
num= int(input("enter the number:"))

count=0
while count<5:
    d=2
    while d<num:
      if num%d==0:
        break
      d=d+1
      if d==num:
       print(num)
       count=count+1
    num=num+1    
'''
