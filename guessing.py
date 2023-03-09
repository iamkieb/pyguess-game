import random


#gamemech

def guessing_game(guessLimit, number):
    random_number = random.randint(1, number)
    try:
        while guessLimit > 0:
            guess = int(input('What is your guess? '))
            guessLimit -= 1
            if random_number == guess:
                print('You got it right!')
                break
            elif guess > number:
                print("Your guess is too high")
                print(f"You have {guessLimit} more chances to guess")
            else:
                print("Wrong!!! Try Again")
                print(f"You have {guessLimit} more chances to guess")
        print("Game Over!")
        print(f"The number was...{random_number}")
    except ValueError:
        print("Only numbers are allowed, don't get too clever!")

#Levels

def easy():
    print("You need to guess a number between 1 and 10, and you have 6 guesses, Let's Go! ")
    guessing_game(6,10)

def medium():
    print("You need to guess a number between 1 and 20, and you have 4 guesses, Let's Go! ")
    guessing_game(4,20)

def hard():
    print("You need to guess a number between 1 and 50, and you have 3 guesses, Let's Go! ")
    guessing_game(3,50)

def try_again():
    again = input("Do you want to play again? Yes / No ")
    if again.upper() == 'YES' :
        welcome()
    elif again.upper() == "NO" : 
        print("Thanks for playing ")
    else:
        print("Say that again...Yes or no? ")
        try_again()


def welcome():
    print("Welcome to Guess the Number")
    difficulty = input("Choose your level - Easy, Medium and Hard? ")
    if difficulty.upper() == "EASY":
        easy()
        try_again()
    elif difficulty.upper() == "MEDIUM":
        medium()
        try_again()
    elif difficulty.upper() == "HARD":
        hard()
        try_again()
    else:
        print("That's not a level! Try again!")
        welcome()
    
welcome()