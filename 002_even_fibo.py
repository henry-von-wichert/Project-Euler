fib = [0,1]
while fib[-1] <= 4000000:
    fib.append(fib[-1]+fib[-2])

summe = 0
for f in fib:
    if f%2 == 0:
        summe += f

print(summe)
