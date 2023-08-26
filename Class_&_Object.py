class Employee:
    def __init__(self,fname, mname, lname, email):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.email = email

    def greet_employee(self):
        return("Welcome to Jibran's club " + self.fname)

emp = Employee("jibran", "Nasir", "Khan", "jibbs1@yahoo.com")
print(emp.greet_employee())

emp1 = Employee("Rama","jacob", "Khan", "ram@Gmail.com")
print(emp1.greet_employee())