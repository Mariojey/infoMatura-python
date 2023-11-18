file = open("szachownice.txt", "r")
chessAreas = file.readlines()
count_chessarea = 0
for row in chessAreas:
    row = row.strip()
    first_row = row[0:8]
    last_row = row[len(row)-8:len(row)]
    if first_row.count('H') > 0  or last_row.count('H') > 0:
        count_chessarea += 1
    for chess_num in range(8, len(row)-8, 8):
        chess_row = row[chess_num:chess_num+8]
        if chess_row[0] == 'H' or chess_row[7] == 'H':
            count_chessarea += 1
print(count_chessarea)