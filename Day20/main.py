def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    return mean

def blankFunction(a, b):
    pass # returns the function without doing anything
    # The pass statement is used as a placeholder for future code

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("The geometric mean of these two numbers is", calculateGmean(a, b))