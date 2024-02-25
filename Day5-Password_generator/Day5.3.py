#THIS PRORAM WILL GIVE THE SUM OF ALL EVEN NUMBERS FROM 1 TO 100

#THIS VARIABLE WOULD BE THE TOTAL WHICH THE EVEN NUMBER WILL BE ACCUMULATED IN
total = 0

#the range funnction here will start counting from 2 but will skipping 2 number like 2 - 4 - 6..... that's because the third number between brackets is 2 
for even in range(2, 102, 2):
   #since the number hold in "even" changes every time those number are being hold in "total" 
   #total += even is a short form of this total = total + even:  
   total += even 

print(total) 