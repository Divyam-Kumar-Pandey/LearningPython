import random

#list of random 3 letter words
lst = ["fas", "fds", "fda", "fde", "fdr", "fdd", "rew", "rty", "rte", "rtr", "rty", "rtd", "gfd", "gfh", "gfg", "gfr", "gft", "gfd", "hgf", "hgt", "hgr", "hgy", "hgf", "hgd", "jkl", "jkt", "jkr", "jkl", "jky", "jku", "poi", "pok", "pol", "pok", "pom", "poh", "zxc", "zxc", "zxc", "zxc", "zxc", "zxc", "vbn", "vbn", "vbn", "vbn", "vbn", "vbn", "mnb", "mnb", "mnb", "mnb", "mnb", "mnb", "qwe", "qwe", "qwe", "qwe", "qwe", "qwe", "rty", "rty", "rty", "rty", "rty", "rty", "uio", "uio", "uio", "uio", "uio", "uio", "asd", "asd", "asd", "asd", "asd", "asd", "fgh", "fgh", "fgh", "fgh", "fgh", "fgh", "jkl", "jkl", "jkl", "jkl", "jkl", "jkl", "zxc", "zxc", "zxc", "zxc", "zxc", "zxc", "vbn", "vbn", "vbn", "vbn", "vbn", "vbn", "mnb", "mnb", "mnb", "mnb", "mnb", "mnb", "qwe", "qwe", "qwe", "qwe", "qwe", "qwe", "rty", "rty", "rty", "rty", "rty", "rty", "uio", "uio", "uio", "uio", "uio", "uio", "asd", "asd", "asd", "asd", "asd", "asd", "fgh", "fgh", "fgh", "fgh", "fgh", "fgh"]


def encode(message):
    if(len(message) >= 3):
        return random.choice(lst) + message[1:] + message[:1] + random.choice(lst)
    else:
        # return "".join(reversed(message))
        return message[::-1]
    
def decode(secretCode):
    if(len(secretCode) >= 3):
        return secretCode[-4:-3] + secretCode[3:-4]
    else:
        return secretCode[::-1]
    
a = input("Enter a message: ")
option = input("Enter 1 to encode or 2 to decode: ")
if option == "1":
    print("Encoded message:", encode(a))
elif option == "2":
    print("Decoded message:", decode(a))
else:
    print("Invalid option")

