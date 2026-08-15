

### 1. Write a Python program to create a basic decorator that prints a line of "=" * 20 before and after executing the function.
#Input:
#Welcome to Python
#Output:
#====================
#Welcome to Python
#====================
#Explanation:
#The decorator should print a separator line before and after the original function.
def decfun(c):
    def innerfun():
        print("="*20)
        c()

        print("="*20)
    return innerfun
@decfun
def gret():
 print("Welcome to python")
gret()
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
### 2. Write a Python program to create a basic decorator that converts the string returned by a function into uppercase.
#Input:
#Hello Batch-85
#Output:
#HELLO BATCH-85
#Explanation:
#The decorator should execute the function, take the returned string, convert it to uppercase using upper(), and print the modified string.
def decfun(fun):
    def innerfun():
        y=fun()
        return y.upper()

    return innerfun
@decfun

def gret():
    s="hello batch-85"
    return s
print(gret())
'----------------------------------------------------------------------------------------------------------------------------------------------------------------'
### 3. Write a Python program to create a basic decorator that prints the length of the string returned by the function.
#Input:
#Programming
#Output:
#Programming
#11
#Explanation:
#The decorator should execute the function, print its returned string, and then print its length.

def deffun(fun):
    def innerfun():
        j=fun()
        print(j)
        return len(j)
    return innerfun

@deffun
def gret():
  y="programming"
  return y
print(gret())

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------'
### 4. Write a Python program using Closure to create a function that checks whether a given string ends with a fixed suffix.
#Input:
#Suffix = "ing"
#String = "Programming"
#Output:
#True
#Explanation:
#Create an outer function that stores the suffix and returns an inner function to check whether any given string ends with that suffix.
def suffix(check):
 def innerfun(text):
     return text.endswith(check)
 
 return innerfun

text=input("enter the text")
check=input("enter the suffix")
ch=suffix(check)
print(ch(text))

'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

# 5. Write a Python program to find the longest word whose characters are all unique in a given sentence.
#Input:
#level world python amazing apple
#Output:
#python
#Explanation:
#A word is considered valid if no character repeats within the word. Among all valid words, print the longest one. If multiple valid words have the same maximum length, print the first one.



s="level world python amazing apple"
words=s.split()
longest=""
for i in words:
    if len(i)==len(set(i)):
        if len(i)> len(longest):
          longest=i

print(longest)


















