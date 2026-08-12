'''
1.Write a program to remove duplicates from a list using set?
Input:[1, 2, 2, 3, 3, 3]
Output: [1, 2, 3]'''
a=[1, 2, 2, 3, 3, 3]

print(list(set(a)))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''2.Return sorted elements of a set?remove duplicates from a list using setfind the first element that is present in the list but missing in the tuple?count how many perfect numbers are present in both the list and the tuple, count how many element
Input: {3, 1, 2}
Output: [1, 2, 3]'''
Input={3, 1, 2}
print(list(Input))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''3.Write a Python program to count how many elements are common among three sets?
Sample Input:
A = {2, 4, 6, 8}
B = {4, 6, 8, 10}
C = {1, 4, 6, 12}
Sample Output:2'''
A = {2, 4, 6, 8}
B = {4, 6, 8, 10}
C = {1, 4, 6, 12}
common = A & B & C
print("Count:", len(common))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
4.Write a Python program to count how many perfect numbers are present in both the list and the tuple?
Sample Input:
List  = [6, 12, 28, 20]
Tuple = (6, 28, 30, 496)
Sample Output:2'''
List  = [6, 12, 28, 20]
Tuple = (6, 28, 30, 496)
count = 0  
for i in List:
    if i in Tuple:
        total=0
        for j in range(1,i//2+1):
            if i%j==0:
                total=total+j
        if total==i:
            count=count+1
print(count)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
5.Write a Python program to find the first element that is present in the list but missing in the tuple?count how many perfect numbers are present in both the list and the tuple, count how many elements are common among three sets
Sample Input:
List  = [15, 20, 25, 30]
Tuple = (20, 30, 40)
Sample Output:15'''
List  = [15, 20, 25, 30]
Tuple = (20, 30, 40)
         
for i in List:
   if i not in Tuple:
       print(i)
       break
    





































