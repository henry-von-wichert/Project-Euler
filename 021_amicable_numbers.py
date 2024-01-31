def divisors(n):
    divs = []
    for x in range(1, int(n/2 + 2)):
        if n%x == 0:
            divs.append(x)
    return divs
    

def divsum(n):
    dsum = 0
    divs = divisors(n)
    for x in divs:
        dsum += x
    return dsum

amicables = []

for n in range(1, 10001):
    divsum1 = divsum(n)
    divsum2 = divsum(divsum1)
    if divsum2 == n:
        if not divsum1 == n:
            amicables.append(n)

amsum = 0

for x in amicables:
    amsum += x

print(amsum)