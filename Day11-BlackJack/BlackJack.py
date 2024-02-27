import random
from os import system
from ASCII_art import logo



def total(chosen_cards: list):
    """Returns the total number that the cards adds up to."""
    total = 0
    specials = ['J', 'K', 'Q']
    for i in chosen_cards:
        if i in specials:
            total += 10
        elif i == "A":
            if total <= 10:
                total += 12
            else:
                total += 1
        else:
            total += i
    return total

def deal_card():
    """Deals a rondom card from the cards deck"""
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10 , 'J', 'K', 'Q']
    card = random.choice(cards)
    return card

if __name__ == "__main__":
    answer = "yes"
    dealer_cards = []
    player_cards = []

    # *While loop to ask the user if he wants to play
    while answer == "yes":
        system('cls')
        print(logo)
        print("Welcom To BlackJack!!\n")
        a = input("Type 's' if you want to start, type 'e' if you want to exit: ")
        if a != 's':
            answer = 'no'
            break

        choice = '1'
        # *deals 2 cards randomly show the players cards and one dealer card
        player_cards = [deal_card(), deal_card()]
        player_total = total(player_cards)
        print("\nyour cards are: {} | Your current total is: {}\n".format(player_cards, player_total))

        dealer_cards = [deal_card(), deal_card()] 
        dealers_total = total(dealer_cards)
        print("the dealer's card is: [{}]".format(dealer_cards[0]))

        # *ask the user if he wants to 'hit' or 'stand' (you might need to use recursion)
        while player_total <= 21 and choice == '1':
            choice = input("\nType '1' if you wan't to 'hit' | Type '2' if you want to 'stand': ")
            if choice == '2':
                break
            else:
                player_cards.append(deal_card())
                player_total = total(player_cards)
                print("\nyour cards are: {} | Your current total is: {}".format(player_cards, player_total))

        # *check if the players exceeds 21
        if player_total > 21:
            print("\nYou Lost!! You exceeded 21")

        # *add to the dealers cards if he hasn't achived 17 yet
        else:
            while dealers_total < 17: 
                dealer_cards.append(deal_card())
                dealers_total = total(dealer_cards)

        # *reveals the winner or state it if it's a draw.
            print("The dealer's cards are {} | The dealer's total is {}".format(dealer_cards, dealers_total)) 
            if dealers_total > 21:
                print("\nYou Win!!")
            elif dealers_total > player_total:
                print("\nYou Lost!!")
            elif player_cards > dealers_total:
                print("\nYou Win!!")
            else:
                print("\nIt's a Draw")


        # * ask the user if he wants to play again (use recursion) and clear.
        answer = input("\nWould you like to play again (yes / no): ")

