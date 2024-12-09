def read_file(file_name):
    print(file_name)
    with open(file_name, "r") as file:
        text = file.read()
    return text


class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def get(self):
        return self.count


def main(file_name):
    xmas_count = Counter()
    text = read_file(file_name)

    text = text.split("\n")
    text = [list(x) for x in text]

    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == "X":
                # Right
                if j + 3 < len(text[i]):
                    if (
                        text[i][j + 1] == "M"
                        and text[i][j + 2] == "A"
                        and text[i][j + 3] == "S"
                    ):
                        xmas_count.add()
                # Left
                if j - 3 >= 0:
                    if (
                        text[i][j - 1] == "M"
                        and text[i][j - 2] == "A"
                        and text[i][j - 3] == "S"
                    ):
                        xmas_count.add()
                # Up
                if i - 3 >= 0:
                    if (
                        text[i - 1][j] == "M"
                        and text[i - 2][j] == "A"
                        and text[i - 3][j] == "S"
                    ):
                        xmas_count.add()
                # Down
                if i + 3 < len(text):
                    if (
                        text[i + 1][j] == "M"
                        and text[i + 2][j] == "A"
                        and text[i + 3][j] == "S"
                    ):
                        xmas_count.add()
                # Diagonal up-right
                if i - 3 >= 0 and j + 3 < len(text[i]):
                    if (
                        text[i - 1][j + 1] == "M"
                        and text[i - 2][j + 2] == "A"
                        and text[i - 3][j + 3] == "S"
                    ):
                        xmas_count.add()
                # Diagonal up-left
                if i - 3 >= 0 and j - 3 >= 0:
                    if (
                        text[i - 1][j - 1] == "M"
                        and text[i - 2][j - 2] == "A"
                        and text[i - 3][j - 3] == "S"
                    ):
                        xmas_count.add()
                # Diagonal down-right
                if i + 3 < len(text) and j + 3 < len(text[i]):
                    if (
                        text[i + 1][j + 1] == "M"
                        and text[i + 2][j + 2] == "A"
                        and text[i + 3][j + 3] == "S"
                    ):
                        xmas_count.add()
                # Diagonal down-left
                if i + 3 < len(text) and j - 3 >= 0:
                    if (
                        text[i + 1][j - 1] == "M"
                        and text[i + 2][j - 2] == "A"
                        and text[i + 3][j - 3] == "S"
                    ):
                        xmas_count.add()
    print("XMAS count:", xmas_count.get())


if __name__ == "__main__":
    main("input.txt")
