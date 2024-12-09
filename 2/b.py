# Rewrote some code and added some types to make it more readable

from typing import List

max_issues = 1
gaps = {"max": 3, "min": 1}
files = {"actual": "list.txt", "test": "example.txt"}
testing = False

def is_increasing(lst: List[int]) -> bool:
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

def is_decreasing(lst: List[int]) -> bool:
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            return False
    return True

def check_gaps(lst: List[int]) -> bool:
    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) > gaps["max"] or abs(lst[i] - lst[i - 1]) < gaps["min"]:
            return False
    return True

def is_safe_with_dampener(lst: List[int]) -> bool:
    if is_increasing(lst) or is_decreasing(lst):
        if check_gaps(lst):
            return True
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if is_increasing(new_lst) or is_decreasing(new_lst):
            if check_gaps(new_lst):
                return True
    return False

def read_file(file: str) -> List[List[int]]:
    list1 = []
    with open(file, "r") as f:
        for line in f:
            tempList = [int(i) for i in line.split()]
            list1.append(tempList)
    return list1

def main():
    list1 = read_file(files["actual"])
    if testing:
        list1 = read_file(files["test"])
    safe_count = 0
    for lst in list1:
        if is_safe_with_dampener(lst):
            safe_count += 1
    print(f"Number of safe reports: {safe_count}")

if __name__ == "__main__":
    main()