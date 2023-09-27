file = open('przyklad.txt', 'r')
result_file = open('wyniki6.txt', 'w')
text  = file.readlines()
count = 0
tab = []
for line in text:
    line = line.split()
    count_in_line = 0
    for i in range(0, int((len(line)/2)-1)):
        if line[i] != line[int((len(line)-1)-i)]:
            count_in_line += 1
    if count_in_line > 0:
        count+=1;
result_file.write(str(count))
file.close()
result_file.close()