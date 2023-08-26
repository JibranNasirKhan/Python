try:
    print("Enter your first number: ")
    a = int(input())
    print("Ënter your second number: ")
    b = int(input())
    if b == 0:
        raise Exception("The denominator is 0.")
    print(a/b)
except Exception as e:
    print(e)
    print("In exception block")
else:
    print("outside exception")
finally:
    print("This is printed")