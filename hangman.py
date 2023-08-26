
class Hangman:

    def __init__(self,name):
        self.string = name.upper()
        self.string_underscore = ""
        self.letter_guess  = ""
        self.string_underscore_new = ""
        self.attempt = 12
        self.toGuess = True
    
    def display(self):
        print(self.string)
    
    def create_underscores(self):
        for i in self.string:
            if i==" ":
                self.string_underscore = self.string_underscore + " "
            else:
                self.string_underscore = self.string_underscore + "_"
        print(self.string_underscore)
    
    def guess_letter(self):
        if self.string == self.string_underscore:
                print("YOU WON!!!!")
                self.toGuess = False
        while self.toGuess:
            
            if self.attempt < 2:
                self.toGuess =False
            letter_guess =input("Enter the character:").upper()
            
            if letter_guess is not None and letter_guess.strip():
                
                self.letter_guess = letter_guess
                self.is_letterIn()
            else:
                print("Input cannot be empty. Please provide valid input.")
            
    def is_letterIn(self):
        index_array = []
        if self.not_Already_in():
                if self.letter_guess in self.string:
                    for index,char in enumerate(self.string):
                        if char == self.letter_guess:
                            index_array.append(index)
                    self.replace_characters(index_array,self.letter_guess)
                    # print(self.string_underscore_new)
                    self.guess_letter()

                   
                else:
                    self.attempt_count()
        else:
                self.attempt_count()
        
            
    
    
    def replace_characters(self,index_array,letter):
        to_array = list(self.string_underscore)
        for i in index_array:
            to_array[i] = letter
        self.string_underscore = self.convert(to_array)
        print(self.string_underscore)
    
    def attempt_count(self):
        self.attempt -=1
        if self.attempt > 0:
            print(f"You have {self.attempt} attempts left")
        else:
            print("Hanged")
        
    
    def not_Already_in(self):
        if self.letter_guess in self.string_underscore:
            return False
        else:
            return True
    
    def convert(self,s):
        result = ''.join(s)
        return result


hangman_words = [
            "Ice Cream", "Guitar", "Doctor", "Strawberry", "Egypt",
            "Mahatma Gandhi", "Tiger", "Tennis", "Star Wars", "Brazil",
            "Elephant", "Orange", "Penguin", "Soccer", "Purple",
            "Australia", "Basketball", "Pizza", "Blue", "Flute",
            "Jurassic Park", "Burger", "Dolphin", "Kangaroo", "Pasta",
            "Apple", "Swimming", "Albert Einstein", "Sushi", "Piano",
            "Red", "Marie Curie", "Engineer", "Banana", "Cleopatra",
            "Japan", "Chef", "Titanic", "Canada", "Green",
            "Inception", "Yellow", "Violin", "Artist", "Cricket",
            "Avatar", "Drum", "Leonardo da Vinci", "Ice Cream"]
words_count  = len(hangman_words)

while True:
    user_choice = int(input(f"Pick any number between 1 to {words_count+1} and 0 to exit:")) 
    if user_choice == 0:
        break
    else:
        user_choice -=1
        if user_choice<=words_count:
            hm = Hangman(hangman_words[user_choice])
            hm.create_underscores()
            hm.guess_letter()
        else:
            print("Enter a valid input:")
