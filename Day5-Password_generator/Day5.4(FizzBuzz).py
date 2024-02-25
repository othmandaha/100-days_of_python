#what this programm each number which is divisable by 3 we must write "fizz" and for each number devisable by 5 we must write "Buzz"
#If the number is devisable by both 3 and 5 we must write "FizzBuzz" instead of that number


#we only need to do this for the numbers between 1 and 100, that's why the range is between 1 and 101 (101 is exclusive)
for num in range(1, 101):
    
    #we started with this condition because if we start with another one and it end up true the other conditions won't follow it will stop
    #each number held in "num" will be tested though all this condition stating from this one at the top
    
    if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz") 
    
    elif num % 3 == 0:
        print("Fizz")
    
    elif num % 5 == 0:
            print("Buzz")
    
    else:
        print(num)
       
    