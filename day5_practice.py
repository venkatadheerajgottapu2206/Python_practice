"""
#DAY 5
#File Handling
#1 Create a file and write "Hello World"
a = "Hello Dheeraj Welcome Back"
with open("data.txt","w") as file:
    content=file.write(a)
    #check the text file Whether the data is updated or not

#2 Write multiple lines into a file
a = "Hello Iam Dheeraj
I am learning to manage time
I am learning Python
"
with open("data.txt","w") as file:
    content=file.write(a)
    #check the text file Whether the data is updated or not

#3 Read entire file content
with open("data.txt","r") as file:
    content=file.read()
    #check the text file Whether the data is updated or not
print(content)

#4 Read file line by line
with open("data.txt","r") as file:
    content=file.read()
    #check the text file Whether the data is updated or not
for line in content:
    print(line)

#5 Append data to existing file
a = input()
with open("data.txt","a") as file:
    file.write(f"\n{a}")
    #check the text file Whether the data is updated or nots


#6 Copy content from one file to another
with open("data.txt","r") as file:
    content=file.read()
    #Red the file 
with open("write.txt","w") as file:
    file.write(content)
    #copied it in to the file

#7 Count number of lines, words, characters in a file
# Open the file in read mode
file = open("write.txt", "r")

# Read file content
content = file.read()

# Count lines
lines = content.split("\n")
line_count = len(lines)

# Count words
words = content.split()
word_count = len(words)

# Count characters
char_count = len(content)

# Display results
print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)

# Close the file
file.close()

#8 Student data save to file (name, marks)

a = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78,
    "Sneha": 88,
    "Kiran": 95
}

with open("data.txt","a") as file:
    file.write(f"\n{a}")
    #check the text file Whether the data is updated or not

#9 Search a word in a file
with open("write.txt","r") as file:
    contents=file.read()
#Search for a word 
s_w=input()
if s_w in contents:
    print("Found",s_w)
else:
    print("Not Found")# DAY 5 - File Handling + Exception Handling (Cleaned)

# 1 & 2. Write to file
with open("data.txt", "w") as file:
    file.write("Hello Dheeraj Welcome Back\n")
    file.write("I am learning Python\n")
    file.write("Consistency is key\n")

# 3. Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# 4. Read line by line (Correct way)
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())   # strip() removes extra newline

# 5. Append data
data = input("Enter text to append: ")
with open("data.txt", "a") as file:
    file.write(data + "\n")

# 6. Copy file
with open("data.txt", "r") as source:
    content = source.read()

with open("backup.txt", "w") as target:
    target.write(content)

# 7. Count lines, words, characters
with open("data.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    words = content.split()
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", len(content))

# 8. Student Data (Better Format)
students = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78
}

with open("students.txt", "w") as file:
    for name, marks in students.items():
        file.write(f"{name} - {marks}\n")

# 9. Search word in file
word = input("Enter word to search: ")
with open("data.txt", "r") as file:
    content = file.read()
    if word.lower() in content.lower():
        print(f"'{word}' Found!")
    else:
        print(f"'{word}' Not Found!")

#10 File exists or not check
import os
filname="dat.txt"
if os.path.exists(filname):
    print("Found")
else:
    print("Not Found")


#11. Handle ZeroDivisionError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

#12. Handle FileNotFoundError
try:
    file = open("data.txt", "r")

    content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File does not exist")
#13. Handle ValueError (when taking input) 
try:
    num = int(input("Enter a number: "))

    print("You entered:", num)

except ValueError:
    print("Error: Please enter only integers")

#14. Multiple except blocks 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    file = open("sample.txt", "r")

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

except FileNotFoundError:
    print("File not found")

#15. Try-Except-Finally 
try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program execution completed")

#16. Raise custom exception (optional)
age = int(input("Enter age: "))

if age < 18:
    raise Exception("You are not eligible to vote")

print("Eligible for voting")

"""
# 17 Personal Diary App (Improved Version)
import os
from datetime import datetime
filename = "diary.txt"

while True:
    print("\n=== Personal Diary ===")
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Note")
    print("4. Delete All Notes")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        note = input("Write your note: ").strip()
        if note:  # empty note vaddu
            with open(filename, "a", encoding="utf-8") as file:
                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                file.write(f"[{timestamp}] {note}\n")
            print("✅ Note added successfully!")
        else:
            print("Note cannot be empty!")

    elif choice == "2":
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
            print("\n--- Your Notes ---")
            print(content)
        else:
            print("No notes found yet.")

    elif choice == "3":
        keyword = input("Enter keyword to search: ").strip().lower()
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                notes = file.readlines()
            found = False
            for note in notes:
                if keyword in note.lower():
                    print(note.strip())
                    found = True
            if not found:
                print("No matching notes found.")
        else:
            print("No notes found.")

    elif choice == "4":
        confirm = input("Are you sure you want to delete ALL notes? (yes/no): ").lower()
        if confirm == "yes":
            open(filename, "w").close()
            print("🗑️ All notes deleted successfully!")
        else:
            print("Delete cancelled.")

    elif choice == "5":
        print("Thank you for using Personal Diary! 👋")
        break

    else:
        print("Invalid choice! Please try again.")