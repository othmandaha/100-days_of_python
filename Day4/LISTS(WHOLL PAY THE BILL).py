import random
names = input("Give me everybody's names, separated by a comma. ")


# here anything you specify inside the parentheses after the split function 
# will be used as a spliter when it is written in your string

splited = names.split(", ")

# the variable $splited now is a list

# the len function here is used to count how much data do we have in our list
# we stored that number in a variable
Names_num = len(splited)

# we subtract one because in programming we start conting form 0
Names_num -= 1 

# we use the number of data that we had befor in the random function 
# in order for the random number generated to not to exced the number of data we have in the list
# the random funtion is used inside the [] instead of a number that we chose
# so it choses somthing randomly from ou list
rand_name = splited[random.randint(0, Names_num)]

print(f"{rand_name} will pay the bill!!")

# there is a much simpler way to do all of this
# a random funtion that choses randomly from a list 
# random.choice() between parentheses we specify the name of the list

