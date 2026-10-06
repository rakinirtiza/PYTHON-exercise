name = "Irtiza"

def greet():
    print(name)

greet()

###global variable function
name = "Irtiza"

def greet():
    print("Hello", name)

greet()

####global vs local
name = "Irtiza"

def greet():
    print(name)

def greet():
    name = "Irtiza"
    print(name)


###scope
name = "Irtiza"

def greet():
    print(name)

greet()
print(name)


####global variable value change
count = 10

def change():
    count = 20
    print(count)

change()

print(count)

###global keyword
count = 0

def increase():
    global count
    count = count + 1

increase()

print(count)

###multiple function 
name = "Irtiza"

def show_name():
    print(name)

def change_name():
    global name
    name = "Rakin"

show_name()

change_name()

show_name()


###########practice

discount = 10

def show_discount():
    print("Discount:", discount)

def change_discount():
    global discount
    discount = 20

show_discount()

change_discount()

show_discount()

###################practice
balance = 1000


def show_balance():
    print("Current Balance:", balance)


def withdraw():
    global balance
    balance = balance - 200


show_balance()

withdraw()

show_balance()

