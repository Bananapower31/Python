age = input("How old are you? ")
age_num = int(age)
years_left = 90 - age_num
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left *12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months remaining")