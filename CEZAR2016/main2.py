file = open('dane_6_2.txt', 'r')
answ_file = open('wyniki_6_2.txt', 'w')
#718 linia bez klucza (roboczo: 1)
text = file.readlines()

answ = ''
# b - zmienna użyta czysto na potrzeby testów programu
#b = 1
for i in text:
    line = i.split()
    word = line[0]
    k = int(line[1].strip())
    #answ += str(b)
    #answ += ' '
    for a in word:
        char_ascii = ord(a) - k
        while char_ascii < 65:
            char_ascii += 26
        answ += chr(char_ascii)
    answ += '\n'
    #b+=1
#print(answ)
answ_file.write(answ)
answ_file.close()
file.close()