for i in range(12):
    if(i == 3):
        print("Skipped i = 3")
        continue
    print("5 x", i, "=", 5*i)
    if(i == 10):
        break