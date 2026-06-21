import json

def save_report(filename, report):
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(report, file, indent=4, ensure_ascii=False)