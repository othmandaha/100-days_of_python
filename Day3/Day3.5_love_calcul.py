print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# This function clalled .lower() is used to lower any upper case letters
name1 = name1.lower()
name2 = name2.lower()

# .count() is used to count how many of the specefied character between () is in the data mentiioned before
love_name1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") 
love_name2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

true_name1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") 
true_name2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")


love_name1and2 = love_name1 + love_name2

true_name1and2 = true_name1 + true_name2

score = str(true_name1and2) + str(love_name1and2)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")