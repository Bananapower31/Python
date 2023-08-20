weight = input("What is your weight in kilograms? ")
height = input("What is your height in meters? ")
bmi = int(weight)/(int(height)*int(height))
print("Your BMI is " + str(round(bmi)))