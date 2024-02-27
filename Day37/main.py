def func1():
    try:
        l = [4,8,9,3,7,3]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some Error Occurred")
        return 0
    finally:
        print("This is always executed.") # This line will always be executed, no matter what.

x = func1()

# Use of finally block:
# The finally block is a block of code that will always be executed, no matter what.
# The finally block is used to deallocate resources and perform clean-up operations.
# The finally block is always placed after the except block(s).
# Used to close the file or network connections, etc.