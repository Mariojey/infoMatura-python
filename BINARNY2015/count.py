file = open('liczby.txt', 'r')
text = file.readlines()
file.close()

count = 0
for i in text:
    if i.count("0") > i.count("1"):
        count += 1
print(count)