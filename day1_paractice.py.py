"""
#1 Add,Substract,Multiply,Divide Two Numbers
a=8
b=2
print(f"Add {a} + {b} = {a+b} \nSubstarct {a} - {b} = {a-b}\nMultiply {a} * {b} = {a*b}\nDivide {a} / {b} = {a/b}")
#2 Swap Two variables (with and without using  third Variable
c=a
a=b
b=c
print(f"With using third variable {a,b}")
a=2
b=8
b=a+b
a=b-a
b=b-a
print(f"With out using third Variable {a,b}")
#3 Simple Calculator
a,b=10,2
if a < b:
    print(a+b)
elif a > b:
    print(a-b)
elif a >= b:
    print(a*b)
else:
    print(a/b)
#4 Check Even or Odd 
print("Even" if a%2==0 else "Odd")
#5 Check Positive Negitive or zero
if a < 0:
    print("Negitive")
elif a > 0:
    print("Positive")
else:
    print("Zero")
#6 largest among 3 numbers
a,b,c=10,20,5
if a>b and a>c:
    print("a is largest")
elif b > c and b > a:
    print("b is greater")
else:
    print("C is grater")
#7 check vowel or consonent 
a='v'
print("Vowel" if a.lower() in "aeiou" else "constant")
#8 Student grade System
print("Student max marks = 100")
a=80
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
#9 Simple interest Calculator
principle=10000
rate_of_interest=2
time_in_years=3
Simple_inteterst=(principle*rate_of_interest*time_in_years)/100
print("Simple Intrest",Simple_inteterst)
#10 Compound Interest 
P,r,n,t=10000,0.03,2,4
n1=r/n
m=((1 + (n1))**(n*t))
A=P*m
Ci=A-P
print(Ci)
#11 Area of a cirlce 
r=5
print((22/7)*r*r)
#12 Area of Rectangle 
l=10
b=2
a=l*b
print(a)
#13 Area of Triangle 
b=3
h=5
a=0.5*(b*h)
print(a)
#14 Celcius to Faranheat converter
c=30
F=(c*1.8)+32
print(F)
#15 Check Leap Year
year=2020
if (year%4==0 or  year%400==0) :
    print("leap year")

else:
    print("Not a leap year")
#16 print Multiplication Table 
n=5
for i in range(1,11):
    print(f"5 * {i} = {5*i}")
#17 Sum of first Natural Numbers 
n=7
s=0
for i in range(1,n+1):
    s=s+i
print(s)
#18 Factorial of a Number
n=5
s=1
for i in range(1,n+1):
    s=s*i
print(s)
#19 Voting Eligiblity Checker 
age=19
if age >= 18:
    print("You are eligible ti vote")
else:
    print("You are not eligible to vote")
#20 Discount & Final Price Calculator
dis_percent=10
sp=1000
final_price=(((100-10)/100)*1000)
print(final_price)

#Pattren programing
#21 Square pattren 
n=int(input())
for i in range(n):
    for j in range(n):
        print("1",end=" ")
    print()

#31 Electric city bill calculator
current_reading=150
previous_reading=12
cost_per_unit=3
units_consumed=current_reading-previous_reading
bil_amount=units_consumed*cost_per_unit
print(bil_amount)


"""
#32 BMI calculator
weight=82
height=1.75
BMI=70/(1.75**2)
if BMI < 18.5:
    print("Under Weight")
elif BMI >= 18.5 or BMI <=24.9:
    print("Normal")
elif BMI >=25 or BMI<=29.9:
    print("OverWeight")
elif BMI>30:
    print("Obese")

#33 Simple ATM Simulation Program

balance = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Current Balance: ₹", balance)

    elif choice == '2':
        deposit = float(input("Enter amount to deposit: ₹"))
        balance = balance + deposit
        print("Amount Deposited Successfully!")
        print("Updated Balance: ₹", balance)

    elif choice == '3':
        withdraw = float(input("Enter amount to withdraw: ₹"))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Withdrawal Successful!")
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance!")

    elif choice == '4':
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid Choice! Please try again.")
