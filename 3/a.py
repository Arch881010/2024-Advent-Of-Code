import re

def read_file(file_name):
    print(file_name)
    with open(file_name, "r") as file:
        text = file.read()
    return text


def main(file_name):
    do = False
    total = 0
    text = read_file(file_name)
    # REGEX IS A PAIN, WHY DID I DECIDED TO DO THIS???
    # Regex for reference https://regexr.com/89psp 
    regex = re.compile(r"mul\(\d+,\d+\)", re.IGNORECASE)

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
        found = found.replace("mul(", "")
        found = found.replace(")", "")
        nums = found.split(",")
        total += (int(nums[0]) * int(nums[1]))
        
    print("The total is:", total)        
        