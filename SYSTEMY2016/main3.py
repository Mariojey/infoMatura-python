file = open('liczby.txt', 'r')
text = file.readlines()
save_file = open('wyniki_6_3.txt','w')

count = 0
for line in text:
    sys = line[len(line)-2]
    if int(sys) == 2:
        num = line[:len(line)-2]
        dec_num = int(num, 2)
        if dec_num % 2 == 0:
            count += 1
save_file.write(str(count))
file.close()
save_file.close()
