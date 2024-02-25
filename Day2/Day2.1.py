print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "s" or "S":
    bill = 15
elif size == "m" or "L":
    bill = 20 
elif size == "l" or "L":
    bill = 25

if add_pepperoni == "y" or "Y":
    bill += 2 
if extra_cheese == "y" or "Y":
    bill += 1 

print(f"your final bill is ${bill}")