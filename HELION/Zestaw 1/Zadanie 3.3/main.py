file = open("odcinki.txt", "r")
text = file.readlines()
max_field = [[0,0],[0,0]]
row_num = 0
for line in text:
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    triangle_field = float(((a+b+c)/2)*(((a+b+c)/2)- a)*(((a+b+c)/2) - b)*(((a+b+c)/2) - c))**(1/2)
    print(str(int(row_num+1)) + ' pole - ' + str(triangle_field))
    # if triangle_field > float(max_field[0][1]):
    #     max_field[0] = [row_num+1, triangle_field]
    # if triangle_field > float(max_field[1][1]) and triangle_field < float(max_field[0][1]):
    #     max_field[1] = [row_num+1, triangle_field]
    row_num += 1

