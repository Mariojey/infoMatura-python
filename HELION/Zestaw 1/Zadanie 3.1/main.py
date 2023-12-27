file = open("odcinki.txt","r")
text= file.readlines()
count = 0
for line in text:
    line = line.split()
    if ((int(line[0]) + int(line[1])) > int(line[2])) and ((int(line[1]) + int(line[2])) > int(line[0])) and ((int(line[0]) + int(line[2])) > int(line[1])):
        count += 1
print(count)