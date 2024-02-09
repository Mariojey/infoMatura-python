a = [5,4,1,5,6,8]
for i in range(1, len(a)+1):
    count_i = 0
    for item in a:
        if i == item:
            count_i += 1
    if count_i != 1:
        print("Nie jest")
        break;