"""
#1 Print numbers from 1 to 50
for i in range(1,51):
    print(i)

#2 Print even numbers between 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i)

        
#3 Print odd numbers between 1 to 100
for i in range(1,101):
    if i%2==1:
        print(i)
#4 Sum of first N natural numbers (using both for & while)
#using for loop
s=0
for i in range(1,11):
    s+=i
print(s)
#using while loop
count=0
n=10
s1=0
while count <= n:
    s1=s1+count
    count=count+1
print(s1)
#5 Factorial of a number (using both for & while)
#using for loop
s=1
for i in range(1,6):
    s*=i
print(s)
#using while loop
count=1
n=5
s1=1
while count <= n:
    s1=s1*count
    count=count+1
print(s1)
#6 Multiplication Table 
n=5
for i in range(1,11):
    print(f"5 * {i}={n*i}")
#7 Print all factors of a number
n1=20
for i in range(1,n1):
    if n1%i==0:
        print(i)
#8 Check Prime Number or not
n2=5
if n2< 1:
    print("Not a prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n2%i==0:
            print(" Not Prime")
            break
        else:
            print("Prime")
#9 Count number of digits in a number
n3=123456
count=0
while n3!=0:
    n3=n3//10
    count=count+1
print(count)
#10 Reverse a number (Example: 123 → 321)
n3=123456
count=0
s2=0
while n3!=0:
    s2=s2*10+n3%10
    n3=n3//10
print(s2)

#Pattern Programs (Very Important):
#11 Square pattern
n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
#12 Right angle triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
#13 Inverted Right angle triangle
n=5
for i in range(n,-1,-1):
    for j in range(i):
        print("*",end="")
    print()

#14 Pyramid pattern
n=5
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*"*(2*i-1))

#15 Inverted Pyramid pattern
n=5
for i in range(n,-1,-1):
    print(" " * (n-i),end="")
    print("*"*(2*i-1))

#16 Diamond pattern
n=5
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*"*(2*i-1))
for i in range(n-1,-1,-1):
    print(" " * (n-i),end="")
    print("*"*(2*i-1))

#17 Sum of digits of a number
n=1234
s=0
while n!=0:
    s=s+n%10
    n=n//10
print(s)

#18 Palindrome number check
n=121
s=0
temp=n
while n!=0:
    s=s*10+n%10
    n=n//10
if s==temp:
    print("Palindrome")
else:
    print("Not a palindrome")

#19 Fibonacci series 
n=5
i=0
a,b=0,1
while i<=n:
    print(a)
    a,b=b,a+b
    i=i+1
#20 Amstrong check 
n=153
s=0
temp=n
while n!=0:
    s=s+((n%10)**3)
    n=n//10
if s==temp:
    print("Amstrong")
else:
    print("Not a Amstrong")

"""


