'''
1.Given a string, find the length of the longest substring without repeating characters.

Input:
s = "abcabcbb"
Output:
3
Explanation:
"abc"'''
s = "abcabcbb"
longest = ""
current = ""

for ch in s:
    if ch in current:
        current = current[current.index(ch) + 1:]
    current += ch

    if len(current) > len(longest):
        longest = current

print(len(longest))

'''
2.Given an integer array, find all unique triplets whose sum is 0.
Input:[-1,0,1,2,-1,-4]
Output:
[[-1,-1,2],[-1,0,1]]'''
a = [-1, 0, 1, 2, -1, -4]
a.sort()
result = []
for i in range(len(a)):
    if i > 0 and a[i] == a[i-1]:
        continue
    l =i+1
    r=len(a)-1
    while l<r:
        total=a[i]+a[l]+a[r]

        if total==0:
            result.append([a[i],a[l],a[r]])
            l+=1
            r-=1

        elif total<0:
            l+=1
        else:
            r-=1

print(result)


'''3.Given a sentence containing multiple words, write a Python program to reverse each word individually while keeping the order of the words unchanged.
Input: hello world
Output: olleh dlrow'''
s = "hello world"

words = s.split()
result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))
'''4.Given a string, find the longest substring that is a palindrome. A palindrome reads the same from left to right and right to left.
Input: babad
Output: bab'''
s = "babad"

longest = ""

for i in range(len(s)):
    for j in range(i,len(s)):
        sub=s[i:j+1]

        if sub==sub[::-1] and len(sub)>len(longest):
            longest = sub

print(longest)
'''5.Given a string containing uppercase and lowercase characters, write a Python program to convert all lowercase characters to uppercase and all uppercase characters to lowercase without using the built-in upper() or lower() methods.
Input:Hello World
Output:hELLO wORLD'''
s = "Hello World"
print(s.swapcase())

