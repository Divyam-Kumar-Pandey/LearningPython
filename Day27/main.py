greeting = '''
+-----------------------------------------+
|                Hi there!                |
|    Let's Play Kaun Banega Crorepati     |
|  Please enter your name below to start  |
|                the game                 |
+-----------------------------------------+
'''
print(greeting, end="")
name = input("Name: ")
# print(name)
questions = [
    "What is the capital of India?", 
    "Name the largest planet in our solar system?", 
    "What is the national animal of India?", 
    "What is the national flower of India?", 
    "What is the national game of India?", 
    "What is the national bird of India?", 
    "What is the national tree of India?", 
    "What is the national currency of India?", 
    "What is the national emblem of India?", 
    "What is the national song of India?"
    ]

options = [
    ["Delhi", "Mumbai", "Kolkata", "Chennai"], 
    ["Earth", "Mars", "Jupiter", "Saturn"], 
    ["Lion", "Tiger", "Elephant", "Leopard"], 
    ["Rose", "Lotus", "Sunflower", "Lily"], 
    ["Cricket", "Hockey", "Football", "Badminton"], 
    ["Peacock", "Sparrow", "Pigeon", "Parrot"], 
    ["Banyan", "Neem", "Peepal", "Mango"], 
    ["Rupee", "Dollar", "Euro", "Pound"], 
    ["Lion Capital of Ashoka", "Red Fort", "Qutub Minar", "India Gate"], 
    ["Vande Mataram", "Jana Gana Mana", "Sare Jahan Se Acha", "Ae Mere Watan Ke Logon"]
    ]

answers = ["Delhi", "Jupiter", "Tiger", "Lotus", "Hockey", "Peacock", "Banyan", "Rupee", "Lion Capital of Ashoka", "Jana Gana Mana"]

print(f"\nWelcome {name}! Let's start the game!\n") # f-string
# f-string stands for formatted string
# It is a new way to format strings in Python 3.6 and above
# It is more concise and easier to use
# It is denoted by the letter "f" before the string
# It is used to embed expressions inside string literals

optionToNum = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3
}

totalPrizeMoney = 0

for i in range(10):
    # Question
    currPrizeMoney = 1000*(i+1)
    print(f"Q{i+1}. {questions[i]}\t", f"Prize Money: {currPrizeMoney}")
    print()

    # Options
    for j in ["A", "B", "C", "D"]:
        print(f"{j}. {options[i][optionToNum[j]]}", end="")
        if(optionToNum[j]%2 == 0): 
            for k in range(30 - len(options[i][optionToNum[j]])):
                print(" ", end="")
        else: print()

    # User Input
    answer = input("Choose one option: ")

    # Error Handling
    while answer.upper() not in optionToNum:
        print("Invalid Option! Please choose a valid option!")
        answer = input("Choose one option: ")

    # Check Answer
    if options[i][optionToNum[answer.upper()]] == answers[i]:
        print("Correct Answer!, You have won", currPrizeMoney, "rupees!")
        totalPrizeMoney += currPrizeMoney
        print("Total Prize Money:", totalPrizeMoney)
    else:
        print(f"Wrong Answer! The correct answer is {answers[i]}")
        break
    print()

# Final Result
print("\nGame Over!")
if(totalPrizeMoney > 0):
    print(f"Congratulations {name}! You have won {totalPrizeMoney} rupees!")
else:
    print(f"Sorry {name}! You have won 0 rupees!")

