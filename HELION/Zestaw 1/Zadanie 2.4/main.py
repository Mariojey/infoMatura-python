file = open("szachownice.txt", "r")
chessares = file.readlines()
count_chessarea = 0
for chess_row in chessares:
    chess_row = chess_row.strip()
    for chess_num in range(0, len(chess_row), 8):
        chess_row_line = chess_row[chess_num:chess_num+8]
        if chess_row_line.count('H') > 0:
            if chess_num != 0 and chess_num != 56:
                if chess_row_line[0] != 'H' and chess_row_line[7] != 'H':
                    count_chessarea += 1
print(count_chessarea)