file = open('liczby.txt', 'r')
answ_file = open('wyniki_6_2.txt', 'w')
text = file.readlines()

count_of_result = 0
for line in text:
    line.strip()
    if line[-2] == '4':
        if '0'not in line:
            count_of_result += 1
print(count_of_result)
answ_file.write(str(count_of_result))
