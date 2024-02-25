# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

name1 = name1.lower 
name2 = name2.lower

name1and2_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") +  name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

name1and2_love = name1.count("l") + name1.count("o") + name1.count("v") + name2.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e") 

score = str(name1and2_true) + str(name1and2_love)

print(score)