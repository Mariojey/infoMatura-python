file = open("przedzialy2.txt","r")
destination = open("parsed.txt", "w")
text = file.readlines()
parsedText = ""
for line in text:
    newLine = line.split('\t')
    parsedLine = ""
    for element in newLine:
        parsedLine += element
    parsedText += parsedLine
destination.write(parsedText)
file.close()
destination.close()