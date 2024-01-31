import math

n = math.factorial(100)
digits = [int(x) for x in str(n)]
sum = 0

for x in digits:
    sum += x

print(sum)