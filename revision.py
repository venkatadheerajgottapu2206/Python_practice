# DAY A - Revision Programs (Improved Version)

# 1. Simple Calculator
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    elif operation == '%':
        return num1 % num2
    elif operation == '**':
        return num1 ** num2
    else:
        return "Invalid Operation"

num1, num2 = map(int, input("Enter two numbers: ").split())
operation = input("Enter operation (+, -, *, /, %, **): ")
print(calculator(num1, num2, operation))


# 2. Student Grade System (Improved)
def get_grade(marks):
    if marks > 100 or marks < 0:
        return "Invalid Marks"
    elif marks >= 90:
        return "A Grade"
    elif marks >= 80:
        return "B Grade"
    elif marks >= 70:
        return "C Grade"
    elif marks >= 40:
        return "D Grade"
    else:
        return "Fail"

marks = int(input("Enter marks: "))
print(get_grade(marks))


# 3. Odd or Even Checker
def odd_or_even_checker(num):
    return "Even" if num % 2 == 0 else "Odd"

num = int(input("Enter a number: "))
print(odd_or_even_checker(num))


# 4. Largest among 3 Numbers (Fixed Logic)
def largest_among_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1, num2, num3 = map(int, input("Enter three numbers: ").split())
print(largest_among_three(num1, num2, num3), "is the largest")


# 5. Leap Year Checker (Good, small improvement)
def is_leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 4 == 0 and year % 100 != 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"

year = int(input("Enter year: "))
print(is_leap_year(year))
