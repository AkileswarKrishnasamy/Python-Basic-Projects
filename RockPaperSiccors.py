import random

def game():
    
    play = 'y'
    while play == 'y':
        
        user = input("R for Rock\nP for Paper\nS for Siccors:").lower()
        computer = random.choice(['r','p','s'])

        print(f"Your choice {user}, Computer's choice {computer}")
        if user == computer:
            print("Draw")
        elif user == 'r' and computer == 's':
            print("User wins")
        elif user == 'p' and computer == 'r':
            print("User wins")
        elif user == 's' and computer == 'p':
            print("User wins")
        else:
            print("Computer wins")
        play = input("wanna play again Y for yes and N for no:").lower()



game()