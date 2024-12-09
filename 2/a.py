min_gap = 1
max_gap = 3

list1 = []

testing = 0

total = 0

max_gap = 3
min_gap = 1


def is_increasing(list):
    for i in range(1, len(list)):
        if list[i] > list[i - 1]: 
            return False
    return True


def is_decreasing(list):
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            return False
    return True


testFile = open("example.txt", "r")
actualFile = open("list.txt", "r")

if testing == 1:
    actualFile = testFile

for line in actualFile:
    tempList = []
    for i in line.split():
        tempList.append(int(i))
    list1.append(tempList)

for list in list1:
    is_allowed = False
    if is_increasing(list) or is_decreasing(list):
        is_allowed = True
        for i in range(len(list) - 2):
            i += 1
            left = list[i] - list[i - 1]
            right = list[i] - list[i + 1]

            left = abs(left)
            right = abs(right)

            #print(len(list), left, right, i, i - 1, i + 1, list[i], list[i - 1], list[i + 1])

            if left > max_gap or right > max_gap:
                is_allowed = False
                print("max_gap error")
                break
            if left < min_gap or right < min_gap:
                is_allowed = False
                print("min_gap error")
                break
        else:
            print("Is not strictly increasing or decreasing")

    if is_allowed:
        print("passes")
        print(list)
        total += 1


print(total)
