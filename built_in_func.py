# # max() - Returns the largest item in an iterable
# # min() - Returns the smallest item in an iterable
# # iter() - Returns an iter object
# # Reverse() - Returns a reversed iterator
# # next() - Returns the next item in an iterable
# # slice() - Returns a slice object
# # sorted() - Returns a sorted list
# # sum() - Sums the items of an iterator
# # input() - Allows user to input value
#
# Tuple = (2,3,5,6,7,8,9,1,3)
# a = max(Tuple)
# print(a)
#
# Tuple = (2,3,5,6,7,8,9,1,3)
# b = min(Tuple)
# print(b)
#
# Tuple = (2,3,5,6,7,8,9,1,3)
# a = iter(Tuple)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# Tuple = (2,3,5,6,7,8,9,1,3)
# d = reversed(Tuple)
# # print(next(d))
# # print(next(d))
# # print(next(d))
# # print(next(d))
# # print(next(d))
# for i in d:
#     i + 1
#     print(i)

    # Slice
Tuple = (2,3,5,6,7,8,9,1,3)
d = slice(2,5)
e = slice(2,5,2)
print(Tuple[d])
print(Tuple[e])

# Sort
Tuple = (2,3,5,6,7,8,9,1,3)
e = sorted(Tuple)
print(e)

    # Sum
Tuple = (2,3,5,6,7,8,9,1,3)
f = sum(Tuple)
print(f)

