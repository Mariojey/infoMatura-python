file = open("szachownice.txt", "r")
chessAreas = file.readlines()
count_chessarea = 0
for chess_area in chessAreas:
    chess_c = 0
    chess_area = chess_area.strip()
    for chess_row_num in range(0, len(chess_area), 8):
        chess_row = chess_area[chess_row_num:chess_row_num+8]
        if chess_row.count('H') > 0:
            if chess_row_num == 16 and chess_row[4] != 'H':
                count_chessarea += 1
                chess_c += 1
            if chess_row[4] == 'H' and chess_row_num != 16:
                count_chessarea += 1
                chess_c += 1
            if (chess_row_num == 0 or chess_row_num == 32) and (chess_row[2] == 'H' or chess_row[6] == 'H'):
                count_chessarea += 1
                chess_c += 1
            if (chess_row_num == 8 or chess_row_num == 24) and (chess_row[3] == 'H' or chess_row[5] == 'H'):
                count_chessarea += 1
                chess_c += 1
            if chess_row_num == 40 and (chess_row[1] == 'H' or chess_row[4] == 'H' or chess_row[7] == 'H'):
                count_chessarea += 1
                chess_c += 1
            if chess_row_num == 48 and chess_row[0] == 'H':
                count_chessarea += 1
                chess_c += 1
print(count_chessarea)