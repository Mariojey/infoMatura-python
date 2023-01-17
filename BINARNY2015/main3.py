file = open('liczby.txt', 'r')
result = open('wyniki4.txt', 'w')
text = file.readlines()
file.close()

answ_text = '4.3 '
answ = 0

min_num = 0
nr_min = 0
max_num = 0
nr_max = 0
nr = 1
for i in text:
    dec = 0
    for j in range(len(i.strip())):
        dec += int(i[j])*2**(len(i.strip())-j-1)
    if dec > max_num:
        max_num = dec
        nr_max = nr
    if dec < min_num or min_num == 0:
        min_num = dec
        nr_min = nr
    nr += 1
print(nr_min)
print(min_num)
print(nr_max)
print(max_num)

answ_text += "wiersze"
answ_text += str(nr_min)
answ_text += " - minimalna,"
answ_text += str(nr_max)
answ_text += " - maksymalna"
result.write(answ_text)

result.close()