file = open('sygnaly.txt', 'r')
result = open('w.txt', 'w')
text = file.readlines()

for i in text:
    max_value = 64
    min_value = 91
    i = i[:-1]
    for j in i:
        if (ascii_code := ord(j)) < min_value:
            min_value = ascii_code
        if ascii_code > max_value:
            max_value = ascii_code
    if max_value - min_value <= 10:
        print(i)

file.close()