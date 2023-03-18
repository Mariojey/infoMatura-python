file = open('liczby.txt', 'r')
save_file = open('wyniki_6_4.txt', 'w')
text = file.readlines()

all_value = 0
for line in text:
    if int(line[len(line)-2]) == 8:
        value = line[:len(line)-2]
        value_in_dec = int(value, 8)
        all_value += value_in_dec
save_file.write(str(all_value))
save_file.close()
file.close()
