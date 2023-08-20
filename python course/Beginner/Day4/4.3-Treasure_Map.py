row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n")
print(f"{row2}\n")
print(f"{row3}\n")
position = input("Where do you want to put the treasure? ")
x = int(position[0])
y = int(position[1])
selected_row = map[y - 1]
selected_row[x - 1] = "💰"
print(f"{row1}\n")
print(f"{row2}\n")
print(f"{row3}\n")