N = 6
for i in range(1,N+1):
    silnia = 1
    for j in range(1,i+1):
        silnia *= j
    print(silnia)
# N = 6
# s = [1]
# i = 1
# while s[i] < N:
#      s[i] = s[i-1]*i
# print(s)