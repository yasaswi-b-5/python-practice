



#Write a recursive function to calculate the factorial of a number. • Input: 5 • Output: 120
'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''

#Write a recursive function to count the number of digits in a number. • Input: 12345 • Output: 5
'''
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
print(count_digits(12345))
'''
#Write a recursive function to find the nth Fibonacci number. • Input: 7 • Output: 13
'''
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))
'''
#Write a recursive function to flatten: [1, [2, 3], [4, [5, 6]]] Output: [1, 2, 3, 4, 5, 6]
'''
def flatten(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
data = [1, [2, 3], [4, [5, 6]]]
print(flatten(data))
'''
#Write a generator that generates cubes from 1 to n.
'''
def cubes(n):
    for i in range(1, n + 1):
        yield i ** 3
for value in cubes(5):
    print(value)
'''
#Write a generator that yields each character of a string one at a time. • Input: "Python" • Output: P y t h o n
'''
def characters(text):
    for char in text:
        yield char
for char in characters("Python"):
    print(char)
'''
#Write a generator that produces the first n Fibonacci numbers. • Input: 7 • Output: 0 1 1 2 3 5 8
'''
def fibonacci_generator(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
for value in fibonacci_generator(7):
    print(value, end=" ")
    '''
#Write a generator that yields all prime numbers between 1 and n. • Input: 20 • Output: 2 3 5 7 11 13 17 19

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_generator(n):
    for i in range(1, n + 1):
        if is_prime(i):
            yield i
for prime in prime_generator(20):
    print(prime, end=" ")


    