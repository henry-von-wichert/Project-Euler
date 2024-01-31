from functools import reduce

nd = 4

def cancel(a,b):
    al = [int(n) for n in list(str(a))]
    bl = [int(n) for n in list(str(b))]
    if 0 in al+bl: return False,False
    bbl = bl.copy()
    for d in bl: 
        if d in al: 
            al.remove(d)
            bbl.remove(d)
    return al,bbl

def listtoint(l):
    n = 0
    for i,d in enumerate(l[::-1]):
        n+= 10**i*d
    return n

def check(a,b):
    al,bl = cancel(a,b)
    if not al: return False
    if len(al) == len(str(a)): return False
    return listtoint(al)*b == listtoint(bl)*a

l = []

for b in range(10**(nd-1),10**nd):
    for a in range(10**(nd-1),b):
        if check(a,b):
            l.append((a,b))
            print(a,b,cancel(a,b))

def hcf(a,b):
    if a < b: a,b = b,a # a > b OBdA
    while b:
        a,b = b, a%b
    return a
           
ajf = reduce(lambda i,j: (i[0]*j[0],i[1]*j[1]),l)
ajfhcf = hcf(*ajf)
kurz = (ajf[0]//ajfhcf, ajf[1]//ajfhcf)
print(kurz)

# für 4 stellen: 19/ 38063850383699406297010378944736350519588529623681657834979492540840701532304401422958380200746947658439415042608514761884348006509130874144551787462379984495451883517356144853845255839080552061891831331688472496054816917158512455925305763333078421651446597080928820048727287189576960411644860865597616312818842369816666748424606006661509473352572391893394434967118738840625376221311766460628992000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000