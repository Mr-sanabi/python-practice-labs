# Files + Regex Lab
# Goal: practice reading/writing text files and extracting data with regex.


# =========================
# Gate 2 — file write/read basics
# =========================


def write_text_file(file_path, text):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

# write_text_file("sample.txt", "Hello from Python file writing!")


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content =  file.read()

    return content

# content = read_text_file("sample.txt")
# print(content)


def append_text_file(file_path, text):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text)


append_text_file("sample.txt", "\nSecond line added with append")