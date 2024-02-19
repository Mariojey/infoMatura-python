# NWW
first_num = 1980
second_num = 46
a = first_num
b = second_num
while b!=a:
    if b<a:
        b += second_num
    elif a<b:
        a += first_num
print(a)