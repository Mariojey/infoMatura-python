file = open("przedzialy2.txt", "r")
text = file.readlines()
line_index = 1
row = [1]
count = 0
for line in text:
    parsedLine = line.strip()
    divs = parsedLine.split(',')
    if divs[0][0] == '<':
        if divs[1][len(divs[1])-1] == '>':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
            count_of_primary_number_in_line = 0
            for number_i in range(int(from_char), int(to_char), 1):
                is_prime = True
                for num in range(2,int(number_i)-1,1):
                    if number_i % num == 0:
                        is_prime = False
                if is_prime:
                    count_of_primary_number_in_line += 1
            if count_of_primary_number_in_line > count:
                row = [line_index]
                count =  count_of_primary_number_in_line
            elif count_of_primary_number_in_line == count:
                row.append(line_index)
        elif  divs[1][len(divs[1])-1] == ')':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
            count_of_primary_number_in_line = 0
            for number_i in range(int(from_char), int(to_char)-1, 1):
                is_prime = True
                for num in range(2,int(number_i)-1,1):
                    if number_i % num == 0:
                        is_prime = False
                if is_prime:
                    count_of_primary_number_in_line += 1
            if count_of_primary_number_in_line > count:
                row = [line_index]
                count =  count_of_primary_number_in_line             
            elif count_of_primary_number_in_line == count:
                row.append(line_index)        
    elif divs[1][len(divs[1])-1] == '>':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
            count_of_primary_number_in_line = 0
            for number_i in range(int(from_char)+1, int(to_char), 1):
                is_prime = True
                for num in range(2,int(number_i)-1,1):
                    if number_i % num == 0:
                        is_prime = False
                if is_prime:
                    count_of_primary_number_in_line += 1
            if count_of_primary_number_in_line > count:
                row = [line_index]
                count =  count_of_primary_number_in_line
            elif count_of_primary_number_in_line == count:
                row.append(line_index)  
    elif divs[1][len(divs[1])-1] == ')':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
            count_of_primary_number_in_line = 0
            for number_i in range(int(from_char)+1, int(to_char)+1, 1):
                is_prime = True
                for num in range(2,int(number_i)-1,1):
                    if number_i % num == 0:
                        is_prime = False
                if is_prime:
                    count_of_primary_number_in_line += 1
            if count_of_primary_number_in_line > count:
                row = [line_index]
                count =  count_of_primary_number_in_line
            elif count_of_primary_number_in_line == count:
                row.append(line_index)                
    line_index += 1
print(row)
print(count)           