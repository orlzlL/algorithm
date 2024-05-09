line = input().upper()
newLine = list(set(line))
countArr = []

for char in newLine:
    countArr.append(line.count(char))

if countArr.count(max(countArr)) >= 2:
    print("?")
else:
    print(newLine[countArr.index(max(countArr))])