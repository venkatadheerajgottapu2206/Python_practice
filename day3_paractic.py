"""
#Day 3
#Lists
#1 Create list & print
lst=list(map(int,input().split()))
print(lst)

#2 Access elements (positive & negative indexing)
lst=[1,2,3,4,5,6,7,8,9]
#Positive indexing 
print(lst[1])
#negative indexing
print(lst[-1])

#3 Slicing 
lst=[1,2,3,4,5,6]
print(lst[0:2])

#4 Append, Insert, Remove, Pop, Clear
lst=[1,2,3,4,5,6]
lst.append(7)
print(lst)
lst.insert(2,8)
print(lst)
lst.remove(3)
print(lst)
lst.pop(5)
print(lst)
lst.clear()
print(lst)

#5 Sort and reverse a list 
lst=[1,8,4,5,7,6,2]
n=len(lst)
#sort the list
for i in range(n):
    swapped=False
    for j in range(0,n-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            swapped=True
    if swapped == False:
        break
print(lst)
# Reverse the list
rev_lst=[]
for i in range(n-1,-1,-1):
    rev_lst.append(lst[i])
print(rev_lst)

#6 Find maximum & minimum in list
lst=[1,2,8,6,4,3,5]
#Maximum
maximum=0
for i in lst:
    if i > maximum:
     maximum=i
#Minimum
minimum=maximum
for i in lst:
    if i < minimum:
     minimum=i 
print(maximum,minimum)

#7 Sum of all elements in list
lst=[1,2,8,6,4,7,5]
s=0
for i in lst:
    s=s+i
print(s)

#8 Count occurrences of element
arr=list(map(int,input().split()))
count={}
for i in arr:
    count[i]=count.get(i,0)+1
print(count)

#9 Merge two lists
l1=[1,2,3,4,5,6]
l2=[7,8,9,10,11,12]
print(l1+l2)

#10 Remove duplicates from list
l=[1,1,2,2,3,4,5,6,7,8,9,9,9]
remove_duplicated=[]
for i in l:
    if i not in remove_duplicated:
        remove_duplicated.append(i)

print(remove_duplicated)

#11 Find even & odd numbers from list separately
l=[1,2,3,4,5,6]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#12 List comprehension (squares of numbers)
num=[]
n=int(input())
for i in range(1,n):
    num.append(i*i)
print(num)

#13 Nested List (Matrix)
nested_matrix=[[1,2,3,],
               [4,5,6],
               [7,8,9]]
print(nested_matrix)

#Dictionaries
#14 Create dictionary, access values
dic={1:"Hello",2:"I",3:"Dheeraj"}
print(dic.values())

#15 Add, Update, Delete items
dic={1:"Hello",2:"I",3:"Dheeraj"}
#Add items to Dictionary 
dic[2]="I am"
#Update
dic[4]="Hamsini"
print(dict)
# delete 
dic.pop(3)
print(dic)

#16 Loop through dictionary
dic={1:"Hello",2:"I",3:"Dheeraj"}
for key,values in dic.items():
    print(key,"=",values)

#17 Student marks dictionary
mark_sheet={"hari":50,"ravi":70,"raju":100}
print(mark_sheet)

text = "apple banana apple mango banana apple"

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

#19 Merge two dictionaries  
mark_sheet={"hari":50,"ravi":70,"raju":100}
dic={1:"Hello",2:"I",3:"Dheeraj"}
mark_sheet.update(dic)
print(mark_sheet)



#Strings
#20 String slicing & indexing
s=input()
#Indexing
print(s[0])
#Slicing 
print(s[1:4])

#21 String methods (upper, lower, strip, replace, split, join)
s=input()
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("Dj","MJ"))
print(s.split(" "))
m="Hamsini"
print(s.join(m))

#22 Check palindrome string
s=input()
m=s[::-1]
if s==m:
    print("Palindrome")
else:
    print('Not a Palindrome')

#23 Count no of vowels in a string 
s=input()
count=0
for i in s:
    if i.lower() in "aeiou":
        count+=1
print(count)

#24 Reverse a string
s=input()
print(s[::-1])



"""





