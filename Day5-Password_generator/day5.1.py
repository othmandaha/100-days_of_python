
#we just split the content of the user input which will be turned to a list of strings
student_heights = input("Input a list of student heights ").split()

#this loop will generate numbers starting from zero and counting the items in the list and it will stop in the final item
for n in range(0, len(student_heights)):
  #the range function makes "n" generate integers each time it runs according to the instructions inside()
  #here the loop runs and specifies each item then convert it to an from a string to an integer
  student_heights[n] = int(student_heights[n])


# we create a starting point for the upcoming loop which will add to this numbers 
sum= 0 
number_of_heights = 0 

# "total" is like a variable that changes everytime the loop makes a turn this changes is governed by the list
# "total" at the biginning will be the first item in the loop then it will transform to the next item until the end of the list
for total in student_heights:
  # the sum here is a variable that is holding a number which is 0 at first as we specifies it
  # each time the loop runs the "sum" holds the number contained in "total" and then adds up to it the second time the loop run with the new number and so on and os forth
  sum += total

  #each time the loop runs the number "1" will be added to "number_of_heights" which is 0
  #the loop will run whatever the number of items is in the list. Thereby, if the list has 3 items the loop will run three times.
  #whatever is indented inside the loop will run the number one will added according to the number of items in the list which will give us the aformetioned. 
  number_of_heights += 1
average = sum / number_of_heights 
print(round(average)) 
#Write your code below this row 👇


