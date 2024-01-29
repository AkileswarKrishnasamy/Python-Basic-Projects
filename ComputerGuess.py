import random

def computer_guess(x):
    print("\n\n\nKeep your Desired number in your mind\n\n\n")
    low = 1
    high = x
    ch = ""
    while ch !="c" and high!=low:
        computer = random.randint(low,high)
        print(f"Computer's Guess is {computer}")
        
        user = input("If the guess is correct enter (C) \nIf Too High enter(H) \nIf Too Low enter(L) :").lower()

        if(user == "h"):
            high = computer
        elif(user == "l"):
            low = computer
        elif(user == "c"):
            break




number = int(input("Enter the number highest largest number:"))
computer_guess(number)