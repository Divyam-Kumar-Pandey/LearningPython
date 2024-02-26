# we can make strings either using single quotes or double quotes
firstName = "divyam"
lastName = '"pandey"'
multiLine = '''this
is 
awesome
'''
print(firstName, lastName)
print(multiLine)
print(firstName[0], firstName[3])

for ch in firstName:
    print(ch, end=" ")