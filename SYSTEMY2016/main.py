file = open('liczby.txt', 'r')
answ_file = open('wyniki_6_1.txt', 'w')
text = file.readlines()

count_of_eight = 0
for line in text:
    line.strip()
    if line[-2] == '8':
        count_of_eight += 1
print(count_of_eight)
answ_file.write(str(count_of_eight))
