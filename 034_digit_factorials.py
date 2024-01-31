from math import factorial
s = 0
factl = [factorial(i) for i in range(10)]
for i in range(3,2000000):
    ss = 0
    for j in str(i): ss+=factl[int(j)]
    if ss == i:
        print(ss)
        s+=i

print(s)