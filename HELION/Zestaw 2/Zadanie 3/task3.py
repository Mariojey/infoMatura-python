file = open("temperatury_nowy_york.txt","r")
text = file.readlines()

quantity_of_lines = 0
sum_temp = 0

for line in text:
    line = line.strip().split()
    quantity_of_lines += 1
    sum_temp += int(line[1])
mid = round(sum_temp/quantity_of_lines, 0)
count = 0
for line in text:
    line = line.strip().split()
    if float(line[1]) < mid:
        count += 1
print(count)