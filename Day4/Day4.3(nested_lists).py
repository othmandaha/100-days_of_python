
# we create 3 lists
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

# we put those lists in another list (nested list)
map = [row1, row2, row3]

# we show the user the map first
print(f"{row1}\n{row2}\n{row3}")

# we ask for a two digit number between 
position = input("Where do you want to put the treasure? ")



# we chose the first digite in the string (0) and the second one (1)
# we convert them into integers 
Horizontal = int(position[0])
vertical = int(position[1])

# we specify which row by specify the number of ou nested list 
# the number is in the integer verical we subtract one since in porgramming we start with 0 
# we save ou chosen row (nested list) in a variable 
row = map[vertical - 1]

# then we specify the data that we want to replace with "X" in our priviously chosen row (nested list) 
# the number of the data was saved in $Horizontal then when subtract 1 as always
row[Horizontal - 1] = "X"



print(f"{row1}\n{row2}\n{row3}")