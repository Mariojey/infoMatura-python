file = open('dane_6_3.txt', 'r')
answ_file = open('wyniki_6_3.txt', 'w')
text = file.readlines()

answ = ''

for i in text:
    line = i.split()
    word = line[0]
    encoded = line[1]
    for i in range(len(word)-2):
        a = word[i]
        b = encoded[i]
        if ((ord(word[i-1]) - ord(encoded[i-1])) % 26) != ((ord(a) - ord(b)) % 26):
            if word not in answ:
                answ += word + '\n'
answ_file.write(answ)
file.close()
answ_file.close()