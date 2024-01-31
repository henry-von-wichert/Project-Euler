import math

def divisorGen(n):
    large_divisors = []
    for i in range(1, (int(math.sqrt(n) + 1))):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

#print(list(divisorGen(100)))

x = 1
while True:
    tri = (1/2) * x * (x+1)
    div = list(divisorGen(tri))
    if len(div) > 499:
        print(tri)
        print(x)
        break
    else:
        x += 1