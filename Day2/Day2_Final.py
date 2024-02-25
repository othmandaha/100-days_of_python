print("Welcom to Tip Calculator!!")

# Here we get the input form the user then convert it from a string to a float
Bill = float(input("How much is the bill? $"))

# and the same here to convert string data type to int which stand for integer(number)
Percentage = int(input("what percentage would you give as a Tip 10, 12, or  15? "))
People = int(input("How many people to split the bill? "))

# here instead of doing this 
# new_percenatge = Percentage / 100 
# We've done this to not to change the name of the variable
Percentage /= 100 


Bill = (Bill * Percentage) + Bill 
Bill /= People 

# Here we've chosen just two numbers after the decimal point
# in case we didn't mention how much numbers do we need after the decimal
# the number will become an integer that is rounded to the nearest number
# this aforementioned process can be done during the devision by deviding with // 
Bill = round(Bill,2)

# This one is called fstring it is used to print different data types without the need for converting
print(f"Each person should pay ${Bill}!")