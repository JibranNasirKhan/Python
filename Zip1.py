list1 =['Ïndia','Äustralia','USA', 'UK']
list2 = ["Pune", "Sydney", "New york", "London"]
s = zip(list1,list2)
print(s)
print(list(s))

price = [42,44,65,90,100]
mrp = [48,50,71,98,110]

for x,t in zip(price, mrp):
    print(t-x)

    # as sets are not ordered it will be random matching example below:
    list1 = {'Ïndia', 'Äustralia', 'USA', 'UK'}
    list2 = {"Pune", "Sydney", "New york", "London"}

for x,y in zip(list1, list2):
    print(x,y)