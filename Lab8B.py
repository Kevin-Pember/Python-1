#Part 1
numFile = open("numbers.txt", "w")
for i in range(1,51):
    numFile.write((str(i)+"\n"))
numFile = open("numbers.txt","r")
numStr = numFile.read()
sum = 0;
while "\n" in numStr:
    index = numStr.index("\n");
    sum += int(numStr[0:index])
    numStr = numStr[index+1:]
numFile.close()
print("The sum is:",sum)

#Part 2
rawData = open("sample.txt","r")
i = 0
rawData.seek(0)
currentLine = []
for line in rawData:
    currentLine = line.split()
    for word in currentLine:
        print(word.rstrip(".,?!"))
    i += 1
    print()
rawData.close()