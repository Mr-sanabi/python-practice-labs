import csv

def load_csv(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = []

            for row in reader:
                rows.append(row)

            return rows
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None