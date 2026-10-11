'''6. Write a recursive function to reverse a string without using [::-1].
	Input: "python"
	Output: "nohtyp" '''
def recursive_function(text):
    if text=="":
         return ""
    return recursive_function(text[1:])+text[0]

print(recursive_function("python"))    


'''7. Write a recursive function to calculate the sum of all elements in a list.
	Input: [10, 20, 30, 40]
	Output: 100'''
def recursive_function(numbers):
    if numbers== 0:
        return 0
    return numbers[0]+recursive_function(text[1:])
       
print(recursive_function(text))    


def recursive_function(numbers):

    if numbers == []:
        return 0
    return numbers[0] + recursive_function(numbers[1:])


numbers = [10, 20, 30, 40]
print(recursive_function(numbers))



'''8. Write a recursive function to count how many times a given number appears in a list.
	Input: [2, 5, 2, 8, 2, 9], target 2
	Output: 3'''
def count_number(numbers, target):
    if len(numbers) == 0:
        return 0

    if numbers[0] == target:
        return 1 + count_number(numbers[1:], target)

    return count_number(numbers[1:], target)


numbers = [2, 5, 2, 8, 2, 9]
target = 2
print(count_number(numbers, target))




'''9. Write a recursive function that removes all occurrences of a given character from a string.
	Input: "banana", character "a"
	Output: "bnn" '''
def remove_character(text, character):
    if len(text) == 0:
        return ""

    if text[0] == character:
        return remove_character(text[1:], character)

    return text[0] + remove_character(text[1:], character)


text = "banana"
character = "a"

print(remove_character(text, character))
