for a in range(1, 1001):
    #a_max = 1000-a
    for b in range(1, 1001):
        for c in range(1, 1001):
            if a**2 + b**2 == c**2 :
                print(a,b,c)
                break