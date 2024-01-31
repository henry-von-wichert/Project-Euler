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

abundant = []

for n in range(1, 28124):
    if divsum(n) > n:
        if len(divisors(n)) > 2:
            abundant.append(n)

len_a = len(abundant)
nonsum = []


for n in range(1, 28124):
    count = 0

    for a in abundant:
        b = n - a
        if b in abundant:
            break
        else:
            count += 1
    if count == len_a:
        nonsum.append(n)


print(nonsum)

#sum = 4179871