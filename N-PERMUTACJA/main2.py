a = [5,4,1,5,6,8]
quantity_correct = 0
for i in range(1, 7):
    print(i)
    count_i = 0
    for item in a:
        if i == item:
            count_i += 1
    if count_i > 0:
        quantity_correct += 1
print(6-quantity_correct)