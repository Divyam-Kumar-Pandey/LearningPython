a = "Divyam kUMAR pandey ??????????" #strings are immutable
print(len(a))
print(a.upper()) #this function will return a new string 
print(a.lower())
print(a.rstrip("?"))
# print(a.replace("a", "i"))
print(a.replace("?", ""))
print(a.split())
print(a.capitalize())

print(len(a), len(a.center(50)))
print(a.center(50)) #make the length of str to 50 by adding 33 spaces at the beginning

print(a.count("?"))
print(a.endswith("???", 3, 5)) # we can add a range where we need to check

print(a.find("s"), a.find("?"), a.find("yam"))
# print(a.index("s"), a.index("?"), a.index("yam")) # this gives an error if not found

print(a.isalnum()) # True if contains A-Z, a-z, 0-9
print(a.isalpha()) # True if contains A-Z, a-z
print(a.islower())
print(a.isprintable()) # if string includes \n, \t, etc, it will give False
str1 = "             "
print(str1.isspace()) # gives true
print(a.isspace()) # gives false

print(a.istitle())
print(a.isupper())
print(a.startswith(" "))
print(a.swapcase())
print(a.title())