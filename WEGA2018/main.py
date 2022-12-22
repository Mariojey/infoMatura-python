#Listing zadania 4.1
file = open('sygnaly.txt', 'r')
result = open('wyniki4.txt', 'w')
#==========Odczytywanie danych z pliku========#
# read() po prostu zapisze do zmiennej a split() podzieli tekst wedle wystąpienia \n
#text = file.read()
#text = text.split("\n")

#Prostszy zapis
text = file.readlines()

#Alokacja zmiennych globalnych
answ = "4.1 "

#===========MainOfCode================#
#print(len(text))

#Odczytywanie co 40-linijki z pliku

#(linijka od której zaczynamy, len(text)-ostatnia linijka, 40 - przeskok (wiekośc iteracji))
for i in range(39, len(text), 40):
    print(text[i][9], end="")
    answ += text[i][9]
result.write(answ)

file.close()
result.close()