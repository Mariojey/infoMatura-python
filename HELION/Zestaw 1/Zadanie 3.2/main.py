# NOT COMPLETE
file = open("odcinki.txt","r")
text = file.readlines()
row_value = [[0,0]]
row_num = 0
def isPrime(num):
    isPrimeNum = True
    for i in range(2,int(num-1)):
        if num%i == 0:
            isPrimeNum = False
    return isPrimeNum

for line in text:
    line = line.split()
    line_semiPrime = 0
    line_zero_divs = []
    for i in range(2, int(int(line[0])-1),1):
        if int(line[0])%i == 0:
            if isPrime(i) and isPrime(int(int(line[0])/i)):
                line_zero_divs.append(i)
    if len(line_zero_divs) == 2:
        line_semiPrime += 1
    line_first_divs = []
    for i in range(2, int(int(line[1])-1),1):
        if int(line[1])%i== 0:
            if isPrime(i) and isPrime(int(int(line[1])/i)):
                line_first_divs.append(i)
    if len(line_first_divs) == 2:
        line_semiPrime += 1     
    line_second_divs = []
    for i in range(2, int(int(line[2])-1),1):
        if int(line[2])%i== 0:
            if isPrime(i) and isPrime(int(int(line[2])/i)):
                line_second_divs.append(i)
    if len(line_second_divs) == 2:
        line_semiPrime += 1
    if line_semiPrime > row_value[0][1]:
        row_value[0] = [row_num+1, line_semiPrime]
    elif line_semiPrime == row_value[0][1]:
        row_value.append([row_num+1,line_semiPrime])
    row_num += 1
    print(str(row_num) + ' ilosc ' + str(line_semiPrime))
print(row_value)