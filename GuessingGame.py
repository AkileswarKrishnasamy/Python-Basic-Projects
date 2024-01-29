import random

def guess(number):
    attempts =10;
    while attempts>0:
        user_guess = int(input("Guess the number:"))
        if(number == user_guess):
            print("you have Guessed it right")
            break
        elif(number<user_guess):
            print("Too Big!")
        elif(number>user_guess):
            print("Too Small")
        attemps = attempts-1
        print(f"you have {attempts} left")
    else:
        print("You ran out of Attemps")


x = random.randint(1,100)
guess(x)
