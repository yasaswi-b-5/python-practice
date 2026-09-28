'''1)Find the length of the longest substring that contains no repeated characters.
Input: "abcabcbb" Output: 3 Because the longest substring without repeating characters is: "abc"
2)Write a function is_anagram(str1, str2) that checks whether two strings contain the same characters with the same frequency.
Input: "listen", "silent" Output: True
3)Write a function compress(text) that converts consecutive repeated characters into the character followed by its count.
Input: "aaabbcccc" Output: "a3b2c4"
4)Write a function replace_vowels(text) that replaces each vowel with the next vowel:
a → e e → i i → o o → u u → a Example: Input: "education" Output: "idacetoun"
5)Write a function is_rotation(str1, str2) that checks whether str2 is a rotated version of str1.
Input: "abcd", "cdab" Output: True
'''
def longest_substring(text):
    longest = ""
    for i in range(len(text)):
        current = ""
        for j in range(i, len(text)):
            if text[j] in current:
                break
            current += text[j]
    if len(current) > len(longest):
            longest = current
    return len(longest)
print(longest_substring("abcabcbb"))



def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent"))

def compress(text):
    result = ""
    count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result += text[i] + str(count)
            count = 1
    result += text[-1] + str(count)
    return result
print(compress("aaabbcccc"))



def replace_vowels(text):
    result = ""

    for ch in text:
        if ch == "a":
            result += "e"
        elif ch == "e":
            result += "i"
        elif ch == "i":
            result += "o"
        elif ch == "o":
            result += "u"
        elif ch == "u":
            result += "a"
        else:
            result += ch

    return result


print(replace_vowels("education"))





def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    return str2 in str1 + str1


print(is_rotation("abcd", "cdab"))
