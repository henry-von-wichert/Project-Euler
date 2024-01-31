f = 2
factors = []
n = 600851475143

while f <= n:
    while n%f == 0:
        factors.append(f)
        n = n // f
    f += 1

print(factors)