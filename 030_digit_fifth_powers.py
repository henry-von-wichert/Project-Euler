def dfp(n,power):
    return sum([int(d)**power for d in list(str(n))])

s = 0

maxposs = 1
power = 5
while maxposs* 9**power> 10**maxposs: maxposs +=1
print(f"Maximal: {(mp:=(maxposs-1)* 9**power)}")
for n in range(11,mp):
    if n == dfp(n,power): 
        print(n)
        s+=n

print(f"Summe = {s}")