heights = input("Input a list of student heights ").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])
print(heights)
total_height = 0
#sum()
for height in heights:
    total_height += height
#len()
number_of_heights = 0
for people in heights:
    number_of_heights += 1
#Average
average_height = round(total_height / number_of_heights)
print(average_height)