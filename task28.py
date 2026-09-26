'''Write a function second_character(text) that returns the second occurrence of a character
that is different from the first character. Input: "aaabbc" Output: "b" '''

def second_character(text):
    first = text[0]

    for ch in text:
        if ch != first:
            return ch

print(second_character("aaabbc"))

def second_character(text):
  first=text[0]  
  for ch in text[1:]:
      if ch!=first:
          return ch
  else:  
           return None  

text="aaabbc"
print( second_character(text))

'''Write a function replace_vowels(text) that replaces every vowel with *. Input: "hello world" Output: "h*ll* w*rld" '''

def replace_vowels(text):
    result=""
    for i in text:
        if i in "aeiouAEIOU":
            result=result+'*'
        else:
            result=result+i
    return result
text="hello world"
print(replace_vowels(text))


'''Write a function count_words(text) that counts the words . Input: "Python is very easy" Output: 4'''
def count_words(text):
   count=0 
   for i in text.split():
       count=count+1    
   return count 

text="Python is very easy"
print(count_words(text))


'''Write a function find_longest_word(text) that returns the longest word in a sentence. Input: "Python makes programming easy" Output: "programming" '''

def find_longest_word(text):
    long=""
    for i in text.split():
        if len(i)>len(long):
           long=i
    return long

text="Python makes programming easy"
print(find_longest_word(text))




'''Write a function is_anagram(a, b) that checks whether two strings contain the same characters with the same frequencies. Input: "listen", "silent" Output: True'''
def is_anagram(a, b):
    if sorted(a)==sorted(b):
        return True
    else:
        return False


(a,b)= "listen", "silent"
print(is_anagram(a, b))























