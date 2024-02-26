a = 2
b = "test"
c = True
d = complex(3, 4)
e = 453213.1684654654
print(a, b, c, d, e, sep="\n")
print(type(a), type(b), type(c), type(d), type(e))

# List can store any type of object or items simultaneously, mutable
list = [a, b, c, d, e]
print(list)

tuple = (5, 3, 2) # same as lists, but immutable
# list[0] = e
# print(list)
print(tuple)

dict = {
    "name" : "Divyam",
    "age" : 20,
    "isCoder" : True
}