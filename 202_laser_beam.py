import math

count = 0
n_reflektionen = 491
k_ref = int((n_reflektionen + 3)/2)
k1_ref = int(k_ref+1)

for x in range(1, k1_ref):
    y = k_ref - x
    diff = x-y
    if diff % 3 == 0:
        if math.gcd(x,y) == 1:
            count += 1

print(count)