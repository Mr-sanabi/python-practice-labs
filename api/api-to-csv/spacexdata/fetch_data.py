import requests
import json
import csv

url = "https://api.spacexdata.com/v4/launches"

response = requests.get(url)
data = response.json()

rows = []

for item in data:
    rows.append({
         "Rocket": item["rocket"],
         "Success": item["success"],
         "Failures": item["failures"],
         "Details": item["details"]
         })
    
with open("spacexdata_output.json", "w", encoding="utf-8") as file:
     writer = json.dump(rows, file, indent=4)
     
