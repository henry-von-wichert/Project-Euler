def prime_gen(nmax):
    l = [2]
    for n in range(3,nmax,2):
        mods = {n%p for p in l}
        if 0 not in mods: l.append(n)
    return l

def is_circular(p,ps):
    g = str(p)
    l = len(g)
    c = True
    for i in range(l-1):
        g = g[1:] + g[0]
        if int(g) not in ps: c = False
    return c

ps = prime_gen(1000)
l = [p for p in ps if is_circular(p,ps)]
print(l,len(l))