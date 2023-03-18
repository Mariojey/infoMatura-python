file = open('liczby.txt','r')
save_file = open('wyniki_6_5.txt','w')
text = file.readlines()

max_val_dec=0
min_val_dec=int(text[0][:len(text[0])-2], int(text[0][len(text[0])-2]))
min_val_bin=''
max_val_bin=''
for line in text:
    if int(line[:len(line)-2],int(line[len(line)-2])) > max_val_dec:
        max_val_dec = int(line[:len(line)-2],int(line[len(line)-2]))
        max_val_bin = line
    if int(line[:len(line)-2], int(line[len(line)-2])) < min_val_dec:
        min_val_dec = int(line[:len(line)-2], int(line[len(line)-2]))
        min_val_bin = line
save_file.write(str(max_val_dec)+" maksymalna - dziesiętnie")
save_file.write(max_val_bin+" maksymalna_binarnie")
save_file.write(str(min_val_dec)+" minimalna dziesiętnie")
save_file.write(min_val_bin+" minialna binarnie")
file.close()
save_file.close()
