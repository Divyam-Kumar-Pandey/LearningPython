a = input("Enter a number between 5 and 9: ")

try:
    a = int(a)
except:
    if(a.lower() != "quit" or a.lower() != "exit"):
        raise Exception("You wrote a string instead of integer. If you want to exit, type 'quit' or 'exit'")
    else:
        exit()

if(a < 5 or a > 9):
    raise ValueError("Enter a number b/w 5 and 9")

print("Everything is fine.")
