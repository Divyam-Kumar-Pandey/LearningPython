age = int(input("Enter your age: "))
if(age > 18):
    print("You can vote.")
elif(age == 17):
    print("You should not vote.")
    name = input("Ok\nEnter Your Name: ")
    if(name.lower() == "divyam"):
        print("You can vote.")
    else:
        print("You cannot vote.")
else:
    print("You cannot vote.")