def average(a, b): # here a, b are required 
    return (a+b)/2

def average2(a = 2, b = 8):
    return (a+b)/2

def average3(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    avg = sum/len(numbers)
    # print("The average is", avg)
    return avg

def funcToTakeDict(name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
def funcToTakeDict2(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

dict = {
    'fname' : "Divyam",
    'mname' : "Kumar",
    'lname' : "Pandey"
}

funcToTakeDict(dict)
funcToTakeDict2(fname= "Divyam", mname = "Kumar", lname = "Pandey")
# print(average(4,5))
# print(average2())
# print(average2(4)) 
# print(average2(b = 10))
# print(average2(b = 10, a = 32))
    
print(average3(5,6,4,8,9,3))


'''
Four type of function arguments
- Default Arguments
- Keyword Arguments
- Variable length Arguments
- Required Arguments
'''