'''
1. Write a Python program to create a dictionary containing student names as keys and their marks as values. Display all the key-value pairs?
Sample Input:{'Ravi': 85, 'Priya': 92, 'John': 78}
Sample Output:
Ravi : 85
Priya : 92
John : 78'''
a={'Ravi': 85, 'Priya': 92, 'John': 78}
for i in a:
    print(i,':',a[i])

'''2. Write a Python program to find the student who scored the highest marks in a dictionary?
Sample Input:{'Ravi': 85, 'Priya': 92, 'John': 78}
Sample Output:
Priya'''
a={'Ravi': 85, 'Priya': 92, 'John': 78}
high=0
for i in a:
    if a[i]>high:
        high=a[i]
        name=i
print(name)        
        
'''3. Write a Python program to count the total number of key-value pairs in a dictionary?

Sample Input:{'A': 10, 'B': 20, 'C': 30, 'D': 40}
Sample Output:4'''
a={'A': 10, 'B': 20, 'C': 30, 'D': 40}
print(len(a))

'''4. Write a Python program to calculate the sum of all values in a dictionary?

Sample Input:{'Math': 90, 'Science': 85, 'English': 80}
Sample Output:255'''
a={'Math': 90, 'Science': 85, 'English': 80}
sum=0
for i in a:
    k=a[i]
    sum=sum+k
print(sum)

'''5. Write a Python program to count how many values in a dictionary are even numbers?

Sample Input:{'A': 10, 'B': 15, 'C': 20, 'D': 25}
Sample Output:2'''
a={'A': 10, 'B': 15, 'C': 20, 'D': 25}
count=0
for i in a:
    if a[i]%2==0:
        count=count+1
print(count)        



