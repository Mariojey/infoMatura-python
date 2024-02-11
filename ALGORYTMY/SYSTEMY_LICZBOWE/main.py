def to_Binary(dec, result):
    rest_of_division = dec % 2
    result = str(rest_of_division) + result
    dec = dec//2
    if dec == 1:
        return result
    else:
        to_Binary(dec, result)

A = [7,2,1]
def to_Decimal_using_Horer(pos):
    W = A[0]
    for i in range(1,3):
        W = W * pos + A[i]
    return W
print(to_Decimal_using_Horer(8)) 