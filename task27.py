'''1. Write a function lower(Input) that converts all uppercase English letters (A-Z) into lowercase .
Example:
Input:  "PyThOn"
Output: "python"'''

def lower(Input):
 result=""
 for i in Input:
    if 'A'<=i<='Z':
        result=result+chr(ord(i)+32)
    else:
        result=result+i
 return result  

Input="pyThOn"
print(lower(Input))

'''
2. Write a function upper(Input) that converts lowercase letters (a-z) into uppercase letters without using .upper().
Use ord() and chr().
Example:
Input:  "hello World"
Output: "HELLO WORLD"'''

def upper(Input):
    result=""
    for i in Input:
        if 'a'<=i<='b':
            result=result+char(ord(i)-32)
        else:
            result=result+i
    return result        

Input="hello World"
print(upper(Input))

'''3. Write a function my_capitalize(text) that converts only the first character of a string to uppercase using ASCII values.
Example:
Input:  "python programming"
Output: "Python programming"'''
def my_capitalize(text):
    if 'a'<=text[0]<='z':
        return chr(ord(text[0])-32)+text[1:]
    else:
        return text


Input = "python programming"
print(my_capitalize(Input))






'''4. Write a function analyze_string(text) that counts and returns:
Uppercase characters
Lowercase characters
Digits
Spaces
Special characters
Example:
Input: "PyThon 123!"
Expected result conceptually:
Uppercase: 2
Lowercase: 4
Digits: 3
Spaces: 1
Special: 1'''

def analyze_string(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0
    special = 0

    for ch in text:
        if 'A' <= ch <= 'Z':
            uppercase = uppercase + 1

        elif 'a' <= ch <= 'z':

            lowercase = lowercase + 1

        elif '0' <= ch <= '9':
            digits = digits + 1

        elif ch == ' ':
            spaces = spaces + 1

        else:
            special = special + 1

    return uppercase, lowercase, digits, spaces, special


Input = "PyThon 123!"
result = analyze_string(Input)

print("Uppercase:", result[0])
print("Lowercase:", result[1])
print("Digits:", result[2])
print("Spaces:", result[3])
print("Special:", result[4])


