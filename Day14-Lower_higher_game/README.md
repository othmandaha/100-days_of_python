# Higher or Lower Game 🎮

Welcome to the Higher or Lower game! Test your instincts and guess which Instagram account has more followers. Can you reach the top score?

## How to Play
1. Two Instagram accounts are shown, and you need to guess which one has more followers.
2. Type 'A' if you think the first account has more followers or 'B' if you think the second one does.
3. Keep guessing correctly to increase your score!

## Scoring System 🏆
- Correct Guess: +1 point
- Incorrect Guess: Game Over

## Let's Get Started! 🚀

### Sample Code

```python
from art import logo, vs
from data import data
import random 
from os import system

def prompt_user(a, b):
    """Prompts the user.
    
    Args:
        a (dict): first account information
        b (dict): second account information
    Returns:
        user's answer
    """
    # ... (rest of the function)

def generate_random():
    """returns a random dict from the data list"""
    # ... (rest of the function)

def score_counter(a: dict, b: dict, answer: str):
    """Counts the score.
    
    Args:
        a (dict): first account information 
        b (dict): second account information
        answer (str): the user's answer
    Returns:
        if answere is correct - 1
        otherwise - 2"""
    # ... (rest of the function)

def game():
    """Higher Lower game."""
    # ... (rest of the function)

if __name__ == "__main__":
    game()
