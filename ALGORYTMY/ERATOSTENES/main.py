# METODA NAJBRUTALNIEJSZA
start = 2
stop = 30
numbers = []
for i in range(2,31):
    numbers.append(i)
i = 2
while(i<(stop//2)):
    for num in numbers:
        if num != i and num%i == 0:
            numbers.remove(num)
    i+=1
print(numbers)