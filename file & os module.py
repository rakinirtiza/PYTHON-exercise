##open
file = open("student.txt", "r")
file = open("student.txt", "w")
file = open("student.txt", "a")

##file write
file = open("student.txt", "w")

file.write("My name is Irtiza.")

file.close()

###file read
file = open("student.txt", "r")

content = file.read()

print(content)

file.close()

###with open()
with open("student.txt", "r") as file:
    content = file.read()

print(content)

###file write
with open("student.txt", "w") as file:
    file.write("Name: Irtiza\n")
    file.write("Department: CSE\n")
    file.write("University: AIUB\n")

#####readline
with open("student.txt", "r") as file:
    line = file.readline()

print(line)

###append (new data add)
with open("student.txt", "a") as file:
    file.write("\nUniversity: AIUB")

##########################################################
####os module
import os

###current folder location 
import os
print(os.getcwd())

###current folder file see
import os

print(os.listdir())

###specific folder files
import os

print(os.listdir(r"C:\Users\Irtiza\Desktop"))

###folder create
import os

os.mkdir("student")

#####check folder
import os

if os.path.exists("student"):
    print("Folder exists")
else:
    print("Folder does not exist")

###file delete
import os

os.remove("student.txt")

###folder delete
import os

os.rmdir("student")

###file or folder
import os

print(os.path.isfile("student.txt")) ###true
print(os.path.isdir("student")) ###true

####path create
import os

folder = "student"
file = "data.txt"

path = os.path.join(folder, file)

print(path)



###practice (file & os)



import os

# Create folder
folder_name = "student_data"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Create file path
file_path = os.path.join(folder_name, "student.txt")

# Write student information
with open(file_path, "w") as file:
    file.write("Name: Irtiza\n")
    file.write("Department: CSE\n")
    file.write("University: AIUB\n")

# Read the file
with open(file_path, "r") as file:
    content = file.read()

print("Student Information:")
print(content)

# Show folder path
print("Folder Path:")
print(os.path.abspath(folder_name))
