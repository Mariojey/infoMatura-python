file = open("przedzialy2.txt", "r")
text = file.realines()
first_line = text.strip().split(',')
from_value = [first_line[0][1:]]
to_value = [first_line[1][:-1]]
for line in text:
    parsedLine = line.strip()
    divs = parsedLine.split(',')
    if divs[0][0] == '<':
        if divs[1][len(divs[1])-1] == '>':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
        elif  divs[1][len(divs[1])-1] == ')':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
    elif divs[1][len(divs[1])-1] == '>':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]
    elif divs[1][len(divs[1])-1] == ')':
            from_char = divs[0][1:]
            to_char = divs[1][:-1]   