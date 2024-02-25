#first we import the random modul
import random 

#then we make the variable that'll hold the value of (rock, paper, scissor)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#then we make our list to store our previously created varibles

choices = [rock, paper, scissors]

#here we first asked the user for an input then we convert it to an integer
player_choice_nue = int(input("Tyep 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if player_choice_num >= 3:
    print("You've typed an invalid number!!")
else:
    player_choice = choices[player_choice_num] 




#here we use the random modul to specify a number for us between 0 and 2 which will be the number that will specify the data nedeed inside the list randomly ofc
computer_choice = choices[random.randint(0, 2)]

#the rest is obvious just to giving all the conditions in which the player or the computer will win or lose
if player_choice_num < 3:
    print(f"You chose:\n{player_choice}")
    print(f"Compuer chose:\n{computer_choice}")

    if computer_choice == player_choice:
        print("It's a draw!")

    if computer_choice == choices[0] and player_choice == choices[2]:
        print("You lose!!")

    if computer_choice == choices[1] and player_choice == choices[2]:
        print("You win!!") 

    if computer_choice == choices[2] and player_choice == choices[1]:
        print("You lose!!")

    if player_choice == choices[0] and computer_choice == choices[2]:
        print("You win!!")

    if computer_choice == choices[1] and player_choice == choices[0]: 
        print("You lose!!") 
    
    if player_choice == choices[1] and computer_choice == choices[0]:
        print("You win!!")
