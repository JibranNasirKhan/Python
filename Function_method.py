def addition(x, y):
    print(x + y)

addition(45, 45)
addition(12, 35)

def add (x, y):
    print(x + y)

def sub (x, y):
    print(x - y)

def mul (x, y):
    print(x * y)

def divide (x, y):
    print(x / y)

a = input("enter add if you want to add your numbers :")
x = int(input("Ënter your number : "))
y = int(input("Ënter your number : "))

if a == "add":
    print(add(x,y))
elif a == "+":
    print(add(x,y))
elif a == "-":
    print(sub(x,y))
elif a == "*":
    print(mul(x,y))
elif a == "/":
    print(divide(x,y))
else:
    print("Ënter add to add your numbers")
#

def add(x,y):
    return x+y

z = add(20,25)
print(z)