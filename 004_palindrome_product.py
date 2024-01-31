def is_pal(n):
    strn = str(n)
    back = ""
    for letter in strn:
        back = letter + back
    return back == strn

rec = 0 
for a in range(100,1000):
    for b in range(a,1000):
        if a*b > rec:
            if is_pal(a*b):
                rec = a*b

print(rec)