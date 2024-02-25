print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# chosing only one mathcing condition 
if size == "s":
    bill = 15
elif size == "m":
    bill = 20 
elif size == "l":
    bill = 25

# adding or changing the mathching condition 
if add_pepperoni == "y":
    # here we test the condition to to chose the right output
    if size == "s":
        bill += 2
    else: 
        bill += 3
    
if extra_cheese == "y":
    bill += 1 

print(f"your final bill is ${bill}")