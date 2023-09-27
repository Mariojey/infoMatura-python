file = open('dane.txt', 'r')
result_file = open('wyniki6.txt', 'w')
text  = file.readlines()

min_value = 255
max_value = 0
for line in text:
    for item in line.split():
        if int(item) < min_value:
            min_value = int(item)
        if int(item) > max_value:
            max_value = int(item)
result_file.write('Najjaśniejszy:' + str(max_value))
result_file.write('Najciemniejszy:' + str(min_value))
file.close()
result_file.close()
