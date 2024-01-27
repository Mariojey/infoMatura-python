klucz = [2,3,1]
k = 3
w = ""
s = "OLKRAOOD"
m = 8

def deszyfruj(w, s, m):
    if m % 3 == 0:
        i = 0
        while i < m:
            w += s[i+2]
            w += s[i]
            w += s[i+1]
            i+=3
        return w
    else:
        i = 0
        while i < m - (m % 3):
            w += s[i+2]
            w += s[i]
            w += s[i+1]
            i+=3
        if m % 3 == 2:
            w += s[i+1]
            w += s[i]
        elif m % 3 == 1:
            w += s[i]
        return w
print(deszyfruj(w,s,m))
