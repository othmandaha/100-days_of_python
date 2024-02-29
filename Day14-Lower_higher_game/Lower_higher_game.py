from art import logo, vs
from data import data
import random 
from os import system


def prompt_user(a, b):
    """Prompts the user.
    
    Args:
        a (dict): first account information
        b (dict): secont account information
    Returns:
        user's answer
    """
    print("\nCompare A: {}, a {}, from {}.".format(a['name'], a['description'], a['country']))
    print(vs)
    print("\nAgainst B: {}, a {}, from {}.".format(b["name"], b["description"], b["country"]))

    # Hints to help with devolopment
    print(f"\n\tHint:\n{a['name']}: {a['follower_count']}")
    print(f"{b['name']}: {b['follower_count']}")

    answer = str(input("\n\tWho has more followers (Type A or B): ")).lower()
    return answer


def generate_random():
    """returns a random dict from the data list"""
    return random.choice(data)


def score_counter(a: dict, b: dict, answer: str):
    """Counts the score.
    
    Args:
        a (dict): first account information 
        b (dict): second account information
        answer (str): the user's answer
    Returns:
        if answere is correct - 1
        otherwise - 2"""
    winner = ''
    if a['follower_count'] > b['follower_count']:
        winner = 'a'
    else:
        winner = 'b'
    if answer == winner:
        return 1
    else:
        return 0


def game():
    """Lower higher game."""

    score = 0
    game_over = False

    # keeps running while user is winning
    while game_over == False:
        system('cls')
        print(logo)

        # if run for the first time it sets a and b
        # otherwise it only sets b.
        if score == 0:
            a = generate_random()
            b = generate_random()
        else: 
            print(f"\nYou're Correct! Current score: {score}")
            b = generate_random()

        # User prompt; it gets the answer 
        answer = prompt_user(a, b)

        if score_counter(a, b, answer) == 1:
            score += 1
            a, b = b, a
        else:
            print(f"\nSorry That's wrong! Final score: {score}")
            game_over = True

    # Prompring the user for a replay
    choice = input("\n\tIf you would like to play again type 'y', otherwise type any key. ").lower()
    if choice == 'y':

        game()

if __name__ == "__main__":
    game()
