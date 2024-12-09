def read_file(file_name):
    print(file_name)
    with open(file_name, "r") as file:
        text = file.read()
    return text


def write_log(text):
    with open("output.txt", "a") as file:
        if type(text) == list:
            write_log(
                str(str(text[0]) + "\n" + str(text[1]) + "\n" + str(text[2]) + "\n")
            )
        else:
            file.write(text)


def clear_log():
    with open("output.txt", "w") as file:
        file.write("")


class Counter:
    def __init__(self):
        self.count = 0

    def add(self, n=1):
        self.count += n

    def get(self):
        return self.count


def main(file_name):
    a_count = Counter()
    clear_log()
    # Okay, cool, a is done, but part b is actually asking about "MAS" in an X pattern... thanks advent of code
    # ex:
    # S . M
    # . A .
    # S . M
    # ex2:
    # M . S
    # . A .
    # M . S

    mas_count = Counter()
    text = read_file(file_name)

    text = text.split("\n")
    text = [list(x) for x in text]

    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == "A":
                if (
                    i - 1 >= 0
                    and j - 1 >= 0
                    and j + 1 < len(text[i])
                    and i + 1 < len(text)
                ):
                    ms = [
                        text[i - 1][j - 1] == "M",
                        text[i - 1][j + 1] == "M",
                        text[i + 1][j - 1] == "M",
                        text[i + 1][j + 1] == "M",
                    ]

                    ss = [
                        text[i - 1][j - 1] == "S",
                        text[i - 1][j + 1] == "S",
                        text[i + 1][j - 1] == "S",
                        text[i + 1][j + 1] == "S",
                    ]

                    current_shape = [
                        [text[i - 1][j - 1], ".", text[i - 1][j + 1]],
                        [".", text[i][j], "."],
                        [text[i + 1][j - 1], ".", text[i + 1][j + 1]],
                        ["M Count:", ms.count(True), "S Count:", ss.count(True)],
                    ]

                    if (ms[0] == True and ms[0] == ms[3]):
                        # To prevent double counting
                        ms[0] = False 
                        ms[3] = False
                    if (ms[2] == True and ms[1] == ms[2]):
                        ms[1] = False
                        ms[2] = False
                    


                    if ms.count(True) == 2 and ss.count(True) == 2:

                        print("X-MAS found at", i, j)
                        write_log(current_shape)
                        write_log("X-MAS found at " + str(i) + " " + str(j) + "\n\n")
                        mas_count.add()
                        a_count.add(1)
                    else:
                        # write_log("[REMOVED] \n\n")
                        pass
                        # write_log("X-MAS not found at " + str(i) + " " + str(j) + "\n\n")

    print("MAS count:", mas_count.get())
    print("A count:", a_count.get())


if __name__ == "__main__":
    main("input.txt")
