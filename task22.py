'''
1.Write a function reverse_string(text) that returns the reverse of the given string without using slicing ([::-1])?
Sample Input:Python
Sample Output:nohtyP'''
def reverse_string(text):
     result=""
     for i in range(len(text)-1,-1,-1):
       result=result+text[i]  
     return result
text=input()  
res=reverse_string(text)
print(res)
'''

2.Write a function remove_duplicates(text) that removes duplicate characters while preserving the original order?
Sample Input:programming
Sample Output:progamin'''
def rever(text):
    dup=""
    for i in text:
        if i not in dup:
           dup=dup+i
    return dup
text=input("enter the text:")
result=rever(text)
print(result)

'''
3.Write a function first_unique(text) that returns the first non-repeated character?
Sample Input:swiss
Sample Output:w'''
def first_unique(text):
     for i in text:
        if text.count(i)==1:
            
           return i
text=input()
res=first_unique(text)
print(res)

'''
4.Write a function replace_vowels(text) that replaces every vowel with *?
Sample Input:Python Programming
Sample Output:Pyth*n Pr*gr*mm*ng'''
def replace_vowels(text):
    dup=""
    for i in text:
        if i in "aeiouAEIOU":
           dup+='*'
        else:
            dup+=i
    return dup
text=input()
res= replace_vowels(text)
print(res)

'''
5.Write a function reverse_words(sentence) that reverses every word while keeping the word order unchanged?
Sample Input:Hello Python
Sample Output:olleH nohtyP'''

def reverse_string(text):
     result=""
     for i in text:
       result=result+i[::-1]+' '  
     return result
text=input().split()  
res=reverse_string(text)
print(res)



    
