# Zadanie 1.1

import math

def znajdz_min(t, count):
    min_ = t[0]
    for i in range(0, int(count)):
        if t[i] < min_:
            min_ = t[i]
    return min_
            
def znajdz_max(t, count):
    max_ = 0
    for i in range(len(t)-count, len(t)):
        if t[i] > max_:
            max_ = t[i]
    return max_
            

def zeruj(t, p):
    while len(t) >= 4:
        m = math.floor(len(t)/4)
        min_ = znajdz_min(t, m)
        max_ = znajdz_max(t, m)
        print("min - " + str(min_) + " max - " + str(max_))
        print(t)
        print(p)
        for i in range(0, len(p)):
            if p[i] < min_:
                p[i] = 0
            if p[i] > max_:
                p[i] = 0
        x = []
        for i in range(m, len(t)-m):
            x.append(t[i])
        t = x
        print(p)
t=[1,7,3,3,1,2,8,5,7,2,5,8]
p=[3,8,7,4,2,8,1,9,4,5,7,1]

zeruj(t,p)

