adders = [1]
sides = 100000001
add = 2

while add < sides:
    for i in range(4):
        adders.append(add)
    add += 2

diagonals = []
number = 0

for x in adders:
    number += x
    diagonals.append(number)

diasum = sum(diagonals)

print(diasum)