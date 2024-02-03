file = open("temperatury_nowy_york.txt","r")
text = file.readlines()

prev_temp = 0
daily_max = 0
count = 0
first_day = ''
last_day = ''
first_day_in_iteration = ''
for line in text:
    line = line.strip().split()
    if int(line[1]) >= prev_temp:
        count += 1
        prev_temp = int(line[1])
        if count == 1:
            first_day_in_iteration = line[0]
        if count > daily_max:
            daily_max = count
            first_day = first_day_in_iteration
            last_day = line[0]
    elif int(line[1]) < prev_temp:
        count = 0
        prev_temp = int(line[1])
print(daily_max)
print(first_day)
print(last_day)