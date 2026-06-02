import json
import csv 

with open("dirty.json", "r", encoding="utf-8") as file:
    data = json.load(file)

clean_data = []

for item in data:
    
        row = {
            "id": item.get("id"),
            "name": item.get("name"),
            "price": item.get("price"),
            "stock": item.get("stock"),
            "category": item.get("category"),
                     
        }
        seen_ids = set()
        clean_data = []

        for item in data:
            item_id = item.get("id")

            if item_id not in seen_ids and item["price"] > 100 and item["stock"] > 10:
                seen_ids.add(item_id)
                clean_data.append(item)

with open("cleaned.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "price", "stock", "category"])
    writer.writeheader()
    writer.writerows(clean_data)
