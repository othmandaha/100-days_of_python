
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


BMI = ( int(weight) / (float(height) ** 2) )

BMI = round(BMI, 1)

if BMI < 18.5:
    print(f"your BMI is {BMI},you are underweight")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight!")
elif 25 < BMI < 30:
    print(f"your BMI is {BMI},you are overweight")
elif 30 < BMI < 35:
    print(f"your BMI is {BMI},you are obese") 
else: 
    print (f"your BMI is {BMI}, you're clinically obese")