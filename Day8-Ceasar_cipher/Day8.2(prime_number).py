#Write your code below this line 👇
def prime_checker(number):
    if n != 3 and n != 2:
        if n % 3 == 0 or n % 2 == 0:
            print("It's not a prime number.")
        else: 
            print("It's a prime number.") 
    else: 
        print("It's a prime number")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
