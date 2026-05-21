# 6. Multiplication Table (Small improvement)
def multiplication_table(num, limit=10):
    for i in range(1, limit+1):
        print(f"{num} * {i} = {num * i}")

num = int(input("Enter number for table: "))
multiplication_table(num)


# 7. Sum of first N natural numbers (Fixed)
def sum_natural_numbers(n):
    # Using For loop
    sum_for = 0
    for i in range(1, n+1):
        sum_for += i
    
    # Using While loop
    sum_while = 0
    j = 1
    while j <= n:
        sum_while += j
        j += 1
    
    return sum_for, sum_while

n = int(input("Enter N: "))
print(sum_natural_numbers(n))


# 8. Factorial (Fixed Recursive)
def normal_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def recursive_factorial(n):
    if n == 0 or n == 1:      # Fixed
        return 1
    else:
        return n * recursive_factorial(n-1)

n = int(input("Enter number: "))
print("Normal Factorial:", normal_factorial(n))
print("Recursive Factorial:", recursive_factorial(n))


# 9. Prime Number Check (Major Logic Fix)
def is_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"          # This should be outside the loop

num = int(input("Enter number: "))
print(is_prime(num))


# 10. Fibonacci using Recursion (Good, but added limit)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter n: "))
print(fibonacci(n))
