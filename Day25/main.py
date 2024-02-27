#manipulating tuple
tup = ("Spain", "Russia", "India", "Austria", "USA")
tup1 = tup
print(tup)
temp = list(tup)
temp.append("Finland")
temp.pop(3)
temp[2] = "Canada"
tup = tuple(temp)
print(tup)


tup3 = tup1 + tup # this creates a new tuple
print(tup3)
print(tup3.count("Russia"))
print(tup3.index("India"))