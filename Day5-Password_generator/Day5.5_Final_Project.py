#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


chosen_letters = ""
for letter in range(0, ((int(nr_letters)))):
    chosen_letters += letters[random.randint(0, len(letters))]
    chosen_symbols = ""
for symbol in range(0, ((int(nr_symbols)))):
    chosen_symbols += symbols[random.randint(0, len(symbols))]
chosen_numbers = "" 
for number in range(0, ((int(nr_numbers)))):
    chosen_numbers += numbers[random.randint(0, len(numbers))]
notshuffled = (chosen_letters + chosen_symbols + chosen_numbers)
list_notshuffled = list(notshuffled)
random.shuffle(list_notshuffled)
print(''.join(list_notshuffled))