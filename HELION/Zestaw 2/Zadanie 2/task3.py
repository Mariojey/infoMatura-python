file = open("hieroglify.txt","r")
text = file.readlines()

quantity_of_true = 0
for line_index in range(0,30,6):
    actual = [
        text[line_index].strip().split('\t'),
        text[line_index+1].strip().split('\t'),
        text[line_index+2].strip().split('\t'),
        text[line_index+3].strip().split('\t'),
        text[line_index+4].strip().split('\t')
    ]
    quantity = [0,0,0]
    first_char = actual[0][0]
    for row in actual:
        for item in row:
            if item == "I":
                quantity[0] += 1
            elif item == "II":
                quantity[1] += 1
            elif item == "III":
                quantity[2] += 1
    max_f_char = ""
    if quantity[0] > quantity[1] and quantity[0] > quantity[2]:
        max_f_char = "I"
    elif quantity[1] > quantity[0] and quantity[1] > quantity[2]:
        max_f_char = "II"
    elif quantity[2] > quantity[1] and quantity[2] > quantity[0]:
        max_f_char = "III"
    if quantity[0] == quantity[1] and quantity[0] == quantity[2]:
        if first_char == "I":
            max_f_char = "I"
        elif first_char == "II":
            max_f_char = 'II'
        elif first_char == "III":
            max_f_char = 'III'
    if quantity[0] == quantity[1] and quantity[0] > quantity[2] and quantity[1] > quantity[2]:
        if first_char == "I":
            max_f_char = "I"
        elif first_char == "II":
            max_f_char = 'II'
    if quantity[0] == quantity[2] and quantity[0] > quantity[1] and quantity[2] > quantity[1]:
        if first_char == "I":
            max_f_char = "I"
        elif first_char == "III":
            max_f_char = 'III'
    if quantity[1] == quantity[2] and quantity[1] > quantity[0] and quantity[2] > quantity[0]:
        if first_char == "I":
            max_f_char = "I"
        elif first_char == "II":
            max_f_char = 'II'
    if first_char == max_f_char:
        quantity_of_true += 1
print(quantity_of_true)