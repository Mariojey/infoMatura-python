file = open('dane_6_1.txt', 'r')
result = open('wyniki_6_1.txt', 'w')
text = file.readlines()

answ = ""
k = 107

for i in text:
    for j in i:
        if j != '\n':
            char_ascii = ord(j) + k
            while char_ascii > 90:
                char_ascii -=26
        else:
            char_ascii = ord('\n')
        answ += chr(char_ascii)
result.write(answ)

result.close()
file.close()