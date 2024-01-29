file = open("hieroglify.txt","r")
text = file.readlines()

first_hierogliph = [text[0].strip().split('\t'),
                    text[1].strip().split('\t'),
                    text[2].strip().split('\t'),
                    text[3].strip().split('\t'),
                    text[4].strip().split('\t')]
first_columns = []

for i in range(0,5):
    row = []
    for j in range(0,5):
        row.append(
            first_hierogliph[j][i]
        )
    first_columns.append(row)

quantity_of_premutation = 0
for line_index in range(6,30,6):
    actual = [
        text[line_index].strip().split('\t'),
        text[line_index+1].strip().split('\t'),
        text[line_index+2].strip().split('\t'),
        text[line_index+3].strip().split('\t'),
        text[line_index+4].strip().split('\t')
    ]
    actual_columns = []
    for i in range(0,5):
        row_actual = []
        for j in range(0,5):
            row_actual.append(actual[j][i])
        actual_columns.append(row_actual)
    if_its_fourth_in_first = [[],[],[],[],[]]
    for index_to_check_count in range(0,5):
        if first_columns.count(actual_columns[index_to_check_count]) == 1:
            if_its_fourth_in_first[index_to_check_count] = 1
        elif first_columns.count(actual_columns[index_to_check_count]) == 0:
            if_its_fourth_in_first[index_to_check_count] = 0
    if if_its_fourth_in_first == [1,1,1,1,1]:
        print(actual)