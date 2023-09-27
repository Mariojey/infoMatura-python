# Zadanie 1.2

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
        m = int(len(t)/4)
        min_ = znajdz_min(t, m)
        max_ = znajdz_max(t, m)
        print("min - " + str(min_) + " max - " + str(max_))
        for i in range(0, len(p)):
            if p[i] < min_:
                p[i] = 0
            if p[i] > max_:
                p[i] = 0
        x = []
        for i in range(m, len(t)-m):
            x.append(t[i])
        t = x
    print(zlicz(p))

def zlicz(p):
    count = 0
    i = 0
    while(i < len(p)):
        if p[i] == 0:
            count += 1
        i += 1
    return count

t = []
p = []
for num in range(0,9):
    for push_element in range(0,200):
        t.append(num+1)
        p.append(num+1)
zeruj(t,p)