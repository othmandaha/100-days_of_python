# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
high_score = 0 

#the "high_score" will take the value of "score" if "score" is greater than "high_score"
#let's say the high score is the first item of our list, it will be assigned to "high_score"
#the loop will continue to run casually but if a greater number than the new high_score which was found first and which is the one being compared now is found
#The value of "high_score will be replaced" by the new greater number but in our case it won't because it was the first item in the list
#So the loop will replace score with every item in the list but "high_socre" won't take the value of "score" unless "score" is greater than the current value of "high_score"
for score in student_scores:
  if high_score < score:
    high_score = score 
print(f"The highest score in the class is{high_score}")







#Write your code below this row 👇