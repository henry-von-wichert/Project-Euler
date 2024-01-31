num = ""

for i in range(400000):
    num += str(i)
prod = 1
for i in [1,10,100,1000,10000,100000,1000000]:
    prod *= int(num[i])
print(prod)