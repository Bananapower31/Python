bill = float(input("What is the total bill? $"))
tip = int(input("What percent tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_tip = (bill*(tip/100))+bill
perperson = bill_tip/people
final = round(perperson, 2)
print(f"Each person should pay: ${final}")