a = 27
isPrime = True
i = 2
while i<=(a/2):
    if a % i == 0:
        isPrime = False
    i+=1
print(isPrime)