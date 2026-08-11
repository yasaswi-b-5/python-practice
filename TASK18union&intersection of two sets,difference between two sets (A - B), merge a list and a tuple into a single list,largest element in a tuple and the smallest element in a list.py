'''

1.Write a Python program to find the union of two sets and display the result?union&intersection of two sets,difference between two sets (A - B), merge a list and a tuple into a single list,largest element in a tuple and the smallest element in a list
Sample Input:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
Sample Output:{10, 20, 30, 40, 50, 60}'''
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print((A.union(B)))

'''2. Write a Python program to find the intersection of two sets?
Sample Input:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
Sample Output:{30, 40}'''
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A.intersection(B))

'''3. Write a Python program to find the difference between two sets (A - B)?

Sample Input:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
Sample Output:{10, 20}'''
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A.difference(B))

'''4.Write a Python program to merge a list and a tuple into a single list?
Sample Input:
List  = [10, 20, 30]
Tuple = (40, 50, 60)

Sample Output:[10, 20, 30, 40, 50, 60]'''
List  = [10, 20, 30]
Tuple = (40, 50, 60)
print(List+list(Tuple))

'''5.Write a Python program to find the largest element in a tuple and the smallest element in a list? 
Sample Input:
List  = [15, 8, 30, 12]
Tuple = (45, 10, 60, 25)

Sample Output:
Largest in Tuple = 60
Smallest in List = 8'''
List  = [15, 8, 30, 12]
Tuple = (45, 10, 60, 25)
print("Largest in Tuple=",max(Tuple))
print("Smallest in List=",min(List))



