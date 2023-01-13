file = open('liczby.txt', 'r')

text = file.readlines()

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