file = open("temperatury_nowy_york.txt","r")
text = file.readlines()

daily_max = 0
quantity_of_daily = 0
count = 0
prev = ""
for line in text:
    line = line.strip().split()
    if line[1] == prev:
        count += 1
        if count == daily_max:
            quantity_of_daily += 1
        if count > daily_max:
            daily_max = count
            quantity_of_daily = 1
    else:
        prev = line[1]
        count = 1
print(daily_max)
print(quantity_of_daily)