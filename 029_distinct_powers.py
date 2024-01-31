powers = []
bound = 100

for a in range(2, bound+1):
    for b in range(2, bound+1):
        po = a**b
        if not po in powers:
            powers.append(po)

print(len(powers))