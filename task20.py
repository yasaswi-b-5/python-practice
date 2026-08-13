'''
1.Write a Python program to find the sum of all strong numbers present in a set?
Sample Input:{145, 125, 2, 40585}
Sample Output:40732'''
Input={145, 125, 2, 40585}
total=0
for num in Input:
    i=num
    sum=0
    while i>0:
      d=i%10
      fact=1  
      for j in range(1,d+1):
        fact=fact*j
      sum=sum+fact
      i=i//10
    if sum==num:  
       total=total+num
print(total)

'''2.Write a Python program to find the largest palindrome number in a set?
Sample Input:{11, 22, 121, 88, 99}
Sample Output:121'''
Input={11, 22, 121, 88, 99}
List=[]
for i in Input:
    rev=0
    bkp=i
    while i>0:
        d=i%10
        rev=rev*10+d
        i=i//10
    if  bkp==rev:
     List.append(rev)
max=List[0]     
for i in List:
    if i>max:
        max=i
print(max)




'''3. Write a Python program to find the elements that are common to exactly two sets?
Sample Input:
A = {10, 20, 30, 40}
B = {20, 30, 50, 60}
C = {30, 40, 60, 70}

Sample Output:{20, 40, 60}'''
A = {10, 20, 30, 40}
B = {20, 30, 50, 60}
C = {30, 40, 60, 70}

result = ((A & B) | (B & C) | (A & C)) - (A & B & C)#((20,30)|(30,60)|(30,40)-(30))-->((20,30,40,60)-(30))-->(20,40,60)

print(result)


'''4.Write a Python program to determine whether the union of two sets contains only prime numbers?
Sample Input:
A = {2, 3, 5}
B = {7, 11, 13}
Sample Output:True'''
A = {2, 3, 5}
B = {7, 11, 13}
A.union(B)
for i in A:
    j=2
    if i%j!=0:
      print('True')
      break
    

'''5. Write a Python program to find the sum of all perfect numbers present in the intersection of two sets?
Sample Input:
A = {6, 12, 28, 496}
B = {6, 28, 30, 496}

Sample Output:530
'''
A = {6, 12, 28, 496}
B = {6, 28, 30, 496}
c=A&B
total=0
for n in c:
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i

    if sum==n:
        total=total+n 
print(total)     









    
