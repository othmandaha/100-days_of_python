number = int(input("Which number do you want to check?"))

# The probleme was the equal sign: only 1 
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")