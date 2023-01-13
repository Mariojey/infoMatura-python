file = open('liczby.txt', 'r')
result = open('wyniki4.txt', 'w')
text = file.readlines()
file.close()

answ_text = '4.1 '
answ = 0
for i in text:
    count_of_zero = 0
    count_of_one = 0
    for j in i:
        if j == '0':
            count_of_zero += 1
        elif j == '1':
            count_of_one += 1
    if count_of_zero > count_of_one:
        answ += 1

print(answ)
answ_text += str(answ)
#result.write(answ_text)

result.close()