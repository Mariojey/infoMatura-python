# w — tekst jawny (łańcuch znaków — string),
# s — szyfrogram (łańcuch znaków — string),
# m — długość tekstu jawnego i szyfrogramu (dodatnia liczba naturalna),
# k — liczba elementów klucza (dodatnia liczba naturalna),
# klucz[1..k] — klucz (tablica jednowymiarowa, w której każda z liczb naturalnych
# od 1 do k występuje dokładnie jeden raz).

#KOLORADO
#OLKRAOOD

klucz = [2,3,1]
k = 3
w = "KOLORADO"
s = ""
m = 8
def szyfruj(n):
    if n+k-1<m:
        for i in range(1, k):
            s += w[n+klucz[i-1]-1]
        szyfruj(n+k)
    else:
        while n<=m:
            if n<m:
                s += w[n+1] + w[n]
                n += 2
            else:
                s += w[n]
                n += 1
szyfruj(1)


# PIERWSZE WYWOŁANIE
# n = 1
# 1+3-1<8 TRUE
# i = 1 s += [1+2-1] O
# i = 2 s += [1+3-1] OL
# i = 3 s += [1+1-1] OLK
# DRUGIE WYWOŁANIE 
# n = 1 + 3
# 4 + 3 - 1 < 8 TRUE
# i = 1 s += [4+2-1] OLKR
# i = 2 s += [4+3-1] OLKRA
# i = 2 s += [4+1-1] OLKRAO
# TRZECIE WYWOŁANIE 
# n = 4 + 3
# 7 + 3 - 1 < 8 FALSE
# 7 < 8 TRUE
# s += [8] + [7] OLKRAOOD

# WYNIK PIERWSZEGO LICZBA WYWOŁAŃ = 3, S = OLKRAOOD
