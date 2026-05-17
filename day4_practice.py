"""
#Basic Functions
#1 Add two numbers using function
def add_two_numbers(a,b):
    return a+b
a,b=map(int,input())
print(add_two_numbers(a,b))

#2 Even/Odd checker function
def even_and_odd_checker(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
n=int(input())
print(even_and_odd_checker(n))

#3 Factorial using function (normal + recursive)
#Normal
def factorial_normal(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
#Recursive Style
def factorial_using_recursive_function(n):
    if n==1:
        return 1
    else:
        return n*factorial_using_recursive_function(n-1)
n=int(input())
print(factorial_normal(n))
print(factorial_using_recursive_function(n))

#4 Check Prime number using function
def Check_Prime_number_using_function(n):
    if n==1:
        return "Not a prime"
    else:
        for i in range(2,int(n**0.5)+1,1):
            if n%i!=0:
                return "Prime"
        else:
            print("Not a prime")
n=int(input())
print(Check_Prime_number_using_function(n))

#5 Find Max/Min in list using function
def find_Max_Min_in_list_using_function(lst):
    maximum=lst[0]
    minimum=lst[0]
    for i in range(len(lst)):
        if maximum > lst[i]:
            maximum=lst[i]
        if minimum < lst[i]:
            minimum=lst[i]
    return maximum,minimum
lst=list(map(int,input().split()))
print(find_Max_Min_in_list_using_function(lst))

#6 Calculate Simple & Compound Interest
def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si
def comound_interest(p,t,r,n):
    a=p * (1 + (r / (100 * n))) ** (n * t)
    ci=a-p
    return ci 
p=float(input()) 
t=float(input())
r=float(input()) 
n=float(input())
print(simple_interest(p,t,r))
print(comound_interest(p,t,r,n))

#7 Temperature Converter (C to F and F to C)
def Celsius_to_Fahrenheit(c):
    f=((9/5)*c)+32
    return f
def Fahrenheit_to_Celsius(f):
    c=(5/9)*(f-32)
    return c
c=float(input())
f=float(input())
print(Celsius_to_Fahrenheit(c))
print(Fahrenheit_to_Celsius(f))

#8 Palindrome checker(Number and String)
#number palindrome checker
def pal_num(n):
    temp=n
    s=0
    while n!=0:
        s=s*10+n%10
        n=n//10
    if temp == s:
        return "Palindrome"
    else:
        return "Not a palindrome"
#string palindrome checker
def pal_string(s):
    temp=s[::-1]
    if s==temp:
        return "palindrome"
    else:
        return "Not a palindrome"

n=int(input())
s=input()
print(pal_num(n))
print(pal_string(s))


#Advanced Functions
#9 Function to count vowels & consonants
def function_to_count_vowels_and_consonats(s):
    v=0
    for i in s:
        if i.lower() in "aeiou":
            v+=1
        else:
            c+=1
    return c,v
s=input()
print(function_to_count_vowels_and_consonats(s))

#10 Function to reverse a string
def reverse_a_string(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
s=input()
print(reverse_a_string(s))

#11 Function to calculate factorial using recursion
def factorial(n):
    if n==1:
        return 1
    else:
       return n*factorial(n-1)
n=int(input())
print(factorial(n))

#12 Fibonacci series using recursion
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n))

#13 Function with default arguments 
def greet(a="Hello"):
    return a

print(greet())

#14 Function with *args (sum of all numbers)
def sum_of_num(*m):
    s=0
    for i in m:
        s+=i
    return s
print(sum_of_num(1,2,3,4,5))

#15 Function with **kwargs (student info)
def details(**data):
    for key,value in data.items():
        print(key,value)
details(name="Dheeraj",age=21)

#16 Simple Calculator using functions
def calc(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
a,b=map(int,input().split())
calc(a,b)

#17 ATM operations using functions
def atm(b,wd):
    if wd>b:
        return "Insufficent balance"
    else :
        c_b=b-wd
    return c_b

b,wd=map(int,input().split())
print(atm(b,wd))

#18. Student Grade calculator using function
def student_grade(a):
    if a>90:
     print("A Grade")
    elif a>80:
     print("B Grade")
    elif a>70:
     print("C Grade")
    elif a>60:
     print("D Grade")
    elif a>50:
     print("E Grade")
    elif a<=35:
     print("Fail")
    
print("Student max marks = 100")
a=int(input())
student_grade(a)

# ================= FIXED FUNCTIONS =================

# 4. Prime Number (Corrected)
def is_prime(n):
    if n <= 1:
        return "Not a Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not a Prime"
    return "Prime"

# 5. Max and Min (Corrected)
def find_max_min(lst):
    maximum = lst[0]
    minimum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

# 9. Vowels and Consonants (Fixed)
def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for char in s.lower():
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():        # only alphabets
            consonants += 1
    return vowels, consonants

# 6. Compound Interest (Better Formula)
def compound_interest(p, t, r, n=1):
    amount = p * (1 + (r / (100 * n))) ** (n * t)
    ci = amount - p
    return ci
    

"""
