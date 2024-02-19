first_num = 100
second_num = 15
while first_num != 0 and second_num!=0:
    if first_num>second_num:
        first_num = first_num%second_num
    else:
        second_num = second_num%first_num
print(max(first_num,second_num))