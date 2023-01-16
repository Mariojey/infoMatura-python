file = open('liczby.txt', 'r')
#result = open('wyniki4.txt', 'w')
text = file.readlines()
file.close()

answ_text = '4.1 '
answ = 0

count2 = count8 = 0
for i in text:
    decimal = 0
    for j in range(len(i.strip())):
        decimal += int(i[j])*2**(len(i.strip())-j-1)
    if decimal % 2 == 0:
        count2 += 1
    if decimal % 8 == 0:
        count8 += 1

print(count2)
print(count8)
        
#result.write(answ_text)

#result.close()