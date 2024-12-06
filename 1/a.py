list1 = []
list2 = []

testing = 0

total = 0

testFile = open("example.txt", "r")
actualFile = open("list.txt", "r")

if (testing == 1):
    actualFile = testFile

for line in actualFile:
    splitLine = line.split()
    list1.append(splitLine[0])
    list2.append(splitLine[1])

# Sort the lists
list1.sort()
list2.sort()

for (i, j) in zip(list1, list2):
    print (i, j)
    diff = int(j) - int(i)
    diff = abs(diff)
    total += diff

print(total)

