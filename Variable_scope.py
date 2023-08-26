# Variable scope in Python - boundary of a variable within a program

# local scope
# Global Scope
# global keyword
# LEGB rule: -> Enclosing -> Global -> Built-in

# local scope
def add():
    return x
x = 2
print(add())

# Global Scope
x = 5
def global_scope():
    return x

def global_scope1():
    return x

print(global_scope())
print(global_scope1())

# Global Keyword
# Just by adding global x its become global

def add():
    global x
    return x
x = 2
print(add())

# Global Scope
# x = 5
def global_scope():
    return x

def global_scope1():
    return x

print(global_scope())
print(global_scope1())


def sub():
    x = 20
    print(x)
    def sub1():
        print(x)
        def sub2():
            print(x)
        sub2()
    sub1()
sub()

x = 100
def sub():
    # x = 20
    print(x)
    def sub1():
        print(x)
        def sub2():
            print(x)
        sub2()
    sub1()
sub()