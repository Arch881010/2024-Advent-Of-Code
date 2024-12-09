testing = False
part = "b"

files = {"test": "example.txt", "input": "input.txt"}
current_file = files["input"]

if testing:
    current_file = files["test"]

if part == "a":
    from a import *
elif part == "b":
    from b import *

if __name__ == "__main__":
    main(current_file)