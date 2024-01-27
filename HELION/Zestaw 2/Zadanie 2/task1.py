file = open("hieroglify.txt", "r")
text = file.readlines()

first = [[],[],[],[],[]]

same_quantity = [0,0,0]
squares = [[],[],[]]

for line_index in range(0, 5):
    line = text[line_index].strip().split('\t')
    first[line_index] = line
for line_index in range(6,30,6):
    actual = [text[line_index].strip().split('\t'),
              text[line_index+1].strip().split('\t'),
              text[line_index+2].strip().split('\t'),
              text[line_index+3].strip().split('\t'),
              text[line_index+4].strip().split('\t')]
    local_same_quantity = 0
    for item_id in range(0,5):
        for inner_id in range(0,5):
            if first[item_id][inner_id] == actual[item_id][inner_id]:
                local_same_quantity += 1;
    if local_same_quantity > same_quantity[0]:
        prev = same_quantity[0]
        prev2 = same_quantity[1]
        same_quantity = [local_same_quantity, prev, prev2]
        prev_square = squares[0]
        prev2_square = squares[1]
        squares = [actual, prev_square, prev2_square]
    elif local_same_quantity < same_quantity[0] and local_same_quantity > same_quantity[1]:
        first_quantity = same_quantity[0]
        second_quantity = same_quantity[1]
        same_quantity = [first, local_same_quantity, second_quantity]
        prev_square = squares[0]
        prev2_square = squares[1]
        squares = [prev_square, actual, prev2_square]
    elif local_same_quantity < same_quantity[1] and local_same_quantity > same_quantity[2]:
        same_quantity[2] = local_same_quantity
        squares[2] = actual
print(squares[0])
print((same_quantity[0]*100)/25)
print("---------")
print(squares[1])
print((same_quantity[1]*100)/25)
print("---------")
print(squares[2])
print((same_quantity[2]*100)/25)