def add(x,y):
    return x+y
def subtarct(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def power(x,y):
    return x**y
userchoice=input("enter the type of mathematical operation you want to perform: ")
if userchoice=="add":
    x=int(input("enter first number: "))
    y=int(input("enter second number: "))
    print("result is: ",add(x,y))
elif userchoice=="subtract":
    x=int(input("enter first number: "))
    y=int(input("enter second number: "))
    print("result is: ",subtarct(x,y))
elif userchoice=="multiplication":
    x=int(input("enter first number: "))
    y=int(input("enter second number: "))
    print("result is: ",multiplication(x,y))
elif userchoice=="division":
    x=int(input("enter first number: "))
    y=int(input("enter second number: "))
    print("result is: ",division(x,y))
elif userchoice=="power":
    x=int(input("enter first number: "))
    y=int(input("enter second number: "))
    print("result is: ",power(x,y))
else:
    print("Error: Invalid operation selected. Please choose from add, subtract, multiplication, division, or power.")
# Note: The code above is a simple calculator that performs basic arithmetic operations.