from functools import reduce
file = open("p022_names.txt", "r").read().replace('"','')
names = file.split(",")

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphd = {}
for i,l in enumerate(alph):
    alphd[l] = i+1

def score(name, i):
    global alphd
    name = "0" + name
    s = reduce(lambda x,y: int(x) + alphd[str(y)], list(name))
    s *= i+1
    return s
    


def insertionsort(l):
    new = []
    while len(l) > 0:
        minim = "ZZZZZZZZZZZ"
        ind = 0
        for i, name in enumerate(l):
            if name < minim:
                minim = name
                ind = i
        new.append(l.pop(ind))
    return new

names = insertionsort(names)

summe = 0

for i,name in enumerate(names):
    summe += score(name,i)

print(summe)