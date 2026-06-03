import json
import csv 

with open("spacexdata_output.json", "r", encoding="utf-8") as file:
    data = json.load(file)

rows = []

for item in data:
    failure = item.get("Failures") or []
    
    if failure:
        f = failure[0]
        time = f.get("time")
        altitude = f.get("altitude")
        reason = f.get("reason")
    else:
        time = ""
        altitude = ""
        reason = ""
    row = {
        "Rocket_Id": item.get("Rocket"),
        "Success": item.get("Success"),         
        "Failure_time": time,
        "Failure_altitude": altitude,
        "Failure_reason": reason,
        "Details": item.get("Details")
    }

    rows.append(row)

with open("spacexdata.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Rocket_Id", "Success", "Failure_time", "Failure_altitude", "Failure_reason", "Details"])
    writer.writeheader()
    writer.writerows(rows)
