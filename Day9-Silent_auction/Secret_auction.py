"""A secrete auction program."""
from os import system
from art import gavel


answer = "yes"
participants = {}

while answer == "yes":
    print(gavel)
    print("Welcom to the secret auction program!\n")
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: $"))
    participants[name] = bid
    answer = input("Are there any other bidders?(yes \ no): ")
    system("cls")

biggest_bid = 0.
bidder_name = ''

for key in participants:
    if biggest_bid < participants[key]:
        biggest_bid = participants[key]
        bidder_name = key

print("The winner is {} with a bid of ${}\n".format(bidder_name, biggest_bid))
    