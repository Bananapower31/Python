import random
names_str = input("Give everybody's names, separated by a comma. ")
names = names_str.split(", ")
num_people = len(names)
random_choice = random.randint(0, num_people - 1)
pay = names[random_choice]
print(pay + " is going to buy today.")