file = open('sygnaly.txt', 'r')
result = open('wyniki4.txt', 'w')

text = file.readlines()

answ = "4.2 "

most_different = [text[0], 0]

for i in range(len(text)):
    count_of_different = 0
    record = text[i]
    tab_of_letters = []
    for j in range(len(record)-1):
        if record[j] != record[j-1] and record[j] not in tab_of_letters:
            count_of_different += 1
            tab_of_letters += record[j]
    if count_of_different > most_different[1]:
        most_different = [record, count_of_different]
    print(tab_of_letters)

print(len(most_different[0]))
print(most_different)

answ += str(most_different[0])
answ += str(most_different[1])
print(answ)
result.write(answ)

file.close()
result.close()