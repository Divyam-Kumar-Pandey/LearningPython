# a = input("Enter a number: ")
# print(f"Multiplication table of {a} is:")

# try:
#     for i in range(1, 11):
#         print(f"{a} x {i} = {int(a) * i}")
# except Exception as e:
#     # print(e)
#     print("Please enter a valid number")


# print("Some imp lines of code")
# print("End of the program")

try:
    num = int(input("Enter an Integer: "))
    a = [6, 3, 8]
    print(a[num])

except ValueError:
    print("Entered value is not an integer")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print(e)