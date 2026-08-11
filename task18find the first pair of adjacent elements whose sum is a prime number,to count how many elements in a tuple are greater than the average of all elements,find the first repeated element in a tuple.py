'''6. Write a Python program to find the first repeated element in a tuple?
Sample Input:(10, 20, 30, 20, 40, 50)
Sample Output:20'''
Tuple=(10, 20, 30, 20, 40, 50)
deplicate=[]
for i in Tuple:
    if i not in deplicate:
        deplicate.append(i)
    else:
        print(i)
    

'''7.Write a Python program to count how many elements in a tuple are greater than the average of all elements?
Sample Input:(10, 20, 30, 40, 50)
Sample Output:2'''
elements=(10, 20, 30, 40, 50)
sum=0
count=0
for i in elements:
    sum=sum+i
avg=sum//5
for i in elements:
 if i>avg:
    count=count+1
print(count)



'''8.Write a Python program to find the first pair of adjacent elements whose sum is a prime number
Sample Input:(4, 7, 6, 5, 8)
Sample Output:6 5'''
a = (4, 7, 6, 5, 8)
for i in range(len(a)-1):
    s = a[i] + a[i+1]
    if s > 1:
        prime = True
        for j in range(2, s):
            if s % j == 0:
                prime = False
                break
        
        if prime:
            print(a[i], a[i+1])
            break
