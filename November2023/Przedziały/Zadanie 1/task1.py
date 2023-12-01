file = open("przedzialy.txt", "r")
text = file.readlines()
row_num = 0
count = 0
line_index = 0
for line in text:
    line = line.strip()
    divs = line.split(',')
    if divs[0][0] == '<':
        if divs[1][len(divs[1])-1] == '>':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
            count_of_non_divided_by_two = 0
            for number_i in range(int(from_char), int(to_char), 1):
                if number_i % 2 != 0:
                    count_of_non_divided_by_two += 1
            if count_of_non_divided_by_two > count:
                count = count_of_non_divided_by_two
                row_num = line_index
        else:
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
            count_of_non_divided_by_two = 0
            for number_i in range(int(from_char), int(to_char)-1, 1):
                if number_i % 2 != 0:
                    count_of_non_divided_by_two += 1
            if count_of_non_divided_by_two > count:
                count = count_of_non_divided_by_two
                row_num = line_index
    elif divs[1][len(divs[1])-1] == '>':
        from_char = divs[0][1:]
        to_char = divs[1][:-1]
        count_of_non_divided_by_two = 0
        for number_i in range(int(from_char)+1, int(to_char), 1):
            if number_i % 2 != 0:
                count_of_non_divided_by_two += 1
        if count_of_non_divided_by_two > count:
            count = count_of_non_divided_by_two
            row_num = line_index
    elif divs[1][len(divs[1])-1] == ')':
        from_char = divs[0][1:]
        to_char = divs[1][:-1]
        count_of_non_divided_by_two = 0
        for number_i in range(int(from_char)+1, int(to_char)-1, 1):
            if number_i % 2 != 0:
                count_of_non_divided_by_two += 1
        if count_of_non_divided_by_two > count:
            count = count_of_non_divided_by_two
            row_num = line_index
    line_index += 1
print(row_num)
print(count)