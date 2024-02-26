fullName = "Divyam Kumar Pandey"
print("Length of name is :", len(fullName)) # to calculate length

anotherStr = "mangoAppleBanana"
print(anotherStr[:5]) # gives 5 character from starting (slice from start)
print(anotherStr[5:]) # gives len-5 from end (slice from end)
# slice, divide into two parts
# : -> on left, picks the left one
# : -> on right, picks the right one
print(anotherStr[2:6]) # gives the chars b/w 2 and 6, first < second, otherwise it will print nothing

print(anotherStr[:-2]) # removes from back, positives remove from front.
print(anotherStr[-2:]) # removes from back, positives remove from front.
print(anotherStr[-4:-3]) # gives the chars b/w the 4th char from last and 3 char from last, first one should be bigger in magnitude