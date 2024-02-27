from Art import logo
import random
from os import system


def difficulty_choser():
    """Returns number of attemps available"""
    resolved = False
    attempts = 0
    while resolved == False:
        difficulty = input("\tChose your difficulty, type 'easy' or 'hard': ")
        if difficulty == 'easy':
            attempts = 10
            resolved = True
            break
        elif difficulty == 'hard':
            attempts = 5
            resolved = True
            break
        else:
            print("You've typed something wrong!!\n")
    return attempts


def checker(guess, number):
    """
    Checks the guess comparing it to number.

    Args:
        guess (int): the number guessed by the user.
        number (number): the randoml generated number to be guessed.
    Returns:
    int : 1 if guessed right, 0 otherwise.
    """
    if guess == number:
        print("You got it!! the answer was {}\n".format(number))
        return 1
    elif guess > number: 
        print("Too high\n")
        return 0
    elif guess < number:
        print("Too low\n")
        return 0


def start_game():
    """The Starting poin of the game"""
    system('cls')
    print(logo)
    print("I'm thinking of a number between 1 and 100!")
    number = random.randint(1, 100)
    # print("Pss, the number is {}".format(number))
    game_over = False
    attempts = difficulty_choser()

    while attempts > 0 and game_over == False:
        print("\nYou have {} guesses".format(attempts))
        Guess = int(input("\tMake a guess: "))
        status = checker(Guess, number)
        if status == 1:
            game_over = True
        else:
            attempts -= 1
            if attempts == 0:
                print("You've run out of guesses, you lose!\n")
    
    if input("\tType 'r' to play again, type anything to exit: ") == 'r':
        start_game()


if __name__ == "__main__":
    start_game()








    
        
