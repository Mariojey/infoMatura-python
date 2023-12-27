file = open("odcinki.txt","r")
text = file.readlines()
max_circuit = [0,0]
for line in text:
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    cir = int(a+b+c)
    if cir > max_circuit[1]:
        max_circuit = [1,cir]
    if cir == max_circuit[1]:
        max_circuit = [max_circuit[0]+1, cir]
    print(max_circuit)
print(max_circuit)