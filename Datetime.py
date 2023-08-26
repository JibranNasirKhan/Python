import datetime

a = datetime.datetime.today().date()
b=  datetime.datetime.today().time()
c = datetime.datetime.today()
print(a)
print(b)
print(c)

dateformat = datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
print(dateformat)