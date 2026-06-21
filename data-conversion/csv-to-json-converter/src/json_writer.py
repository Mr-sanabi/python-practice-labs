import json

def save_json(filename, rows):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(rows, file, indent=4, ensure_ascii=False)