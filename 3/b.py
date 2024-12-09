import re

def read_file(file_name):
    print(file_name)
    with open(file_name, "r") as file:
        text = file.read()
    return text

def write_log(text):
    with open("output.txt", "a") as file:
        file.write(text)


def main(file_name):
    do = True
    total = 0
    text = read_file(file_name)
    # REGEX IS A PAIN, WHY DID I DECIDED TO DO THIS???
    # Regex for reference https://regexr.com/89psp 
    regex = re.compile(r"mul\(\d+,\d+\)|(do\(\))|(don't\(\))", re.IGNORECASE)

    found_text = []
    
    loop = True
    while loop:
        match = regex.search(text)
        if match != None:
            found_text.append(match.group())
            text = text[match.end():]
        else:
            loop = False

    for found in found_text:
        if found == "do()":
            do = True
            print("Do is true")
            write_log("Do is true\n")
            continue
        if found == "don't()":
            print("Do is false")
            write_log("Do is false\n")
            do = False
            continue
        if do:
            print("Doing:", found)
            write_log("Doing: " + found + "\n")
            found = found.replace("mul(", "")
            found = found.replace(")", "")
            nums = found.split(",")
            total += (int(nums[0]) * int(nums[1]))
        else:
            print("Skipped:", found)    
            write_log("Skipped: " + found + "\n")
        
    print("The total is:", total)        
        
