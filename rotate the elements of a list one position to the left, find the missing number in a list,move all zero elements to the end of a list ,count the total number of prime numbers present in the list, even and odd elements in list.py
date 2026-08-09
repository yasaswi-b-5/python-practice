
'''1.Write a Python program to separate the even and odd elements of a list into two different lists?
Sample Input: 10 15 22 33 40 55
Sample Output:
Even List: 10 22 40
Odd List: 15 33 55'''
inp=[10,15,22,33,40,55]
even_list=[]
odd_list=[]
for i in  inp :
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print('Even list:',even_list)
print('Odd list:',odd_list)



'''2.Write a Python program to count the total number of prime numbers present in a list?
Sample Input:[2 4 5 9 11 15]
Sample Output:3'''
Input=[2,4,5,9,11,15]
count=0
d=2
for i in Input:
    if i//2%d!=0:
        count=count+1
d=d+1   
print(count)



'''3.Write a Python program to move all zero elements to the end of a list while maintaining the order of the remaining elements?
Sample Input:[2 0 5 0 8 1 0]
Sample Output:[2 5 8 1 0 0 0]'''
Input=[2,0,5,0,8,1,0]
result=[]
for i in Input:
    if i!=0:
        result.append(i)
for i in Input:
    if i==0:
        result.append(i)
print(result)

'''4.Write a Python program to find the missing number in a list?
Sample Input:[1 2 4 5]
Sample Output:3'''
Input=[1,2,4,5]
i=1
while i<=5:
     if i not in Input :
        print(i)
     i+=1

'''5.Write a Python program to rotate the elements of a list one position to the left?

Sample Input:[10 20 30 40 50]
Sample Output:[20 30 40 50 10]'''
Input=[10,20,30,40,50]
x=Input.pop(0)
Input.append(x)
print(Input)


