#string char
name = "Irtiza"
university = "AIUB"
department = "CSE"
name = "Rakin"
email = "rakin@gmail.com"
country = "Bangladesh"
message = "Welcome to Python"

#string length
name = "rakinirtiza"
print(len(name))

#String Indexing
name = "Irtiza"
print(name[0])
print(name[5])

#Negative Indexing
name = "Irtiza"
print(name[-1])
print(name[-4])

#String Slicing
name = "Irtiza"
print(name[2:5])
#or,
name = "Irtiza"
print(name[:3])
#or,
name = "Irtiza"
print(name[2:])

#concatenation
first_name = "RAKIN"
middle_name = "ISRAT"
last_name = "IRTIZA"
full_name =first_name + " " + middle_name + " " + last_name
print(full_name)

#uppercase & lowercase
name = "Irtiza"
print(name.upper())
print(name.lower())

#Capitalize
name = "irtiza"
print(name.capitalize())

#strip()
name = "   Irtiza   "
print(name.strip())

#replace
text = "I love Java"
text = text.replace("Java", "Python")
print(text)

#string if any word
text = "I am learning Python"
print("Python" in text)
print("Java" in text)

#split()
text = "I love Python & my name is irtiza"
words = text.split()
print(words)

#f-string
name = "Rakin Israt Irtiza"
age = 23
print(f"My name is {name} and I am {age} years old.")

#user input+string
name = input("Enter your name: ")
print(f"Hello {name}!")


#######practice 1

name = input("Enter your name: ")
university = input("Enter your university: ")
department = input("Enter your department: ")

print(f"My name is {name}.")
print(f"I study at {university}.")
print(f"My department is {department}.")

##########practice 2

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print(f"Full Name: {full_name}")
print(f"Name Length: {len(full_name)}")
print(f"First Character: {full_name[0]}")
print(f"Last Character: {full_name[-1]}")