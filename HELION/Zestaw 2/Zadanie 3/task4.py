file = open("temperatury_nowy_york.txt","r")
text = file.readlines()

sum_temp = [0,0,0,0,0,0,0]
days_quantity = [0,0,0,0,0,0,0]

for week_index in range(0,182,7):
    week = [
        text[week_index].strip().split(),
        text[week_index+1].strip().split(),
        text[week_index+2].strip().split(),
        text[week_index+3].strip().split(),
        text[week_index+4].strip().split(),
        text[week_index+5].strip().split(),
        text[week_index+6].strip().split()
    ]

    sum_temp[0] += int(week[0][1])
    sum_temp[1] += int(week[1][1])
    sum_temp[2] += int(week[2][1])
    sum_temp[3] += int(week[3][1])
    sum_temp[4] += int(week[4][1])
    sum_temp[5] += int(week[5][1])
    sum_temp[6] += int(week[6][1])

    days_quantity[0] += 1
    days_quantity[1] += 1
    days_quantity[2] += 1
    days_quantity[3] += 1
    days_quantity[4] += 1
    days_quantity[5] += 1
    days_quantity[6] += 1

last = text[182].strip().split()
sum_temp[0] += int(last[1])
days_quantity[0] += 1


print("Piątek:")
print(sum_temp[0]/days_quantity[0])
print("Sobota:")
print(sum_temp[1]/days_quantity[1])
print("Niedziela:")
print(sum_temp[2]/days_quantity[2])
print("Poniedziałek:")
print(sum_temp[3]/days_quantity[3])
print("Wtorek:")
print(sum_temp[4]/days_quantity[4])
print("Środa:")
print(sum_temp[5]/days_quantity[5])
print("Czwartek:")
print(sum_temp[6]/days_quantity[6])