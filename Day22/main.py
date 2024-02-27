l = [5, 6, 8, 9, 8]
print(l)
print(type(l))

#list can contain any type of data types
anotherList = ["divyam", 20, True]
for i in anotherList:
    print(type(i))

print(l[0])

# second number from the end
print(l[-2])
print(l[len(l)-2])
print(l[3])

if 7 in l:
    print("Yes")
else:
    print("No")

# same applies to string as well    
if "yam" in "divyam": print("yes")
if 'y' in "divyam": print("yes")

print(l[1:2])
print(l[1:4:2])

# List Comprehension
lst = [(2*i+1)**2 for i in range(5)]
print(lst)

names = ['Milo', 'Sarah', 'Bruno', 'Anastasia', 'Rosa']
filteredList = [item for item in names if "o" in item]
print(filteredList)