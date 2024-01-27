file = open("hieroglify.txt", "r")
text = file.readlines()

same = []

for line_index in range(0,30,6):
    actual = [
        text[line_index].strip().split('\t'),
        text[line_index+1].strip().split('\t'),
        text[line_index+2].strip().split('\t'),
        text[line_index+3].strip().split('\t'),
        text[line_index+4].strip().split('\t')
    ]
    for line_to_check_index in range(line_index+6,30,6):
        line_to_check = [
            text[line_to_check_index].strip().split('\t'),
            text[line_to_check_index+1].strip().split('\t'),
            text[line_to_check_index+2].strip().split('\t'),
            text[line_to_check_index+3].strip().split('\t'),
            text[line_to_check_index+4].strip().split('\t')
        ]
        if actual == line_to_check:
            same.append([actual, line_to_check])
for item in same:
    print(item[0])
    print(item[1])
    print("---------------------------")