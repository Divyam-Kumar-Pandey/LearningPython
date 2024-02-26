import time
print("Current Time: ", end="")
print(time.strftime('%H:%M:%S %p'))

hour = int(time.strftime('%H'))
if(hour >= 6 and hour < 12):
    print("GOOD MORNING")
elif(hour >= 12 and hour < 16):
    print("GOOD AFTERNOON")
elif(hour >= 16 and hour < 21):
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")
