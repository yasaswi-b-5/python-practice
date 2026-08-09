'''
1.Write a Python program to reverse a list with using any built-in functions like reverse() or slicing.?
   input: list: [10, 20, 30, 40, 50]
   Output: list: [50, 40, 30, 20, 10]'''
list=[10, 20, 30, 40, 50]
list.reverse()
print(list)
'''2.Write a Python program to concatenate two lists with using the built-in extend() method.?
     Input:a = [1, 2, 3]
           b = [4, 5, 6]'''
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
'''3.Write a Python program to insert an element at a specific index in a list.?
     Input:lst = [1, 2, 4]
           index = 2
          value = 3
     output:[1, 2, 3, 4]'''
lst = [1, 2, 4]
lst.insert(2,3)
print(lst)

'''4.Write a Python program to rotate a list to the left by k positions?
      input:lst = [1, 2, 3, 4, 5]
                k = 2 
      output:Rotated List: [3, 4, 5, 1, 2]'''
lst = [1, 2, 3, 4, 5]
k = 2
i = 1
while i <= k:
    x = lst.pop(0)
    lst.append(x)
    i = i + 1
print("Rotated List:", lst)

'''5.Write a Python program to find the index of a specific element in a given list?
input:
my_list = [10, 20, 30, 40, 50]
element = 30
output:The index of 30 is: 2'''

my_list = [10, 20, 30, 40, 50]
my_list.index(30)
print('The index of 30 is:', my_list.index(30))
