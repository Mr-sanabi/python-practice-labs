
# Data Cleaning Pipeline (Python)

This project processes raw JSON data and converts it into a clean CSV dataset.

## Features

- Removes duplicate entries based on unique identifiers (ID)
- Filters data (price > 100, stock > 10)
- Converts JSON to CSV
- Handles structured data cleanly

## Input

Raw JSON file with possible duplicates and inconsistent data.

## Output

Clean CSV file ready for analysis.

## Technologies

- Python
- JSON
- CSV

## Example

Input:
```json
[
  {"id": 2, "name": "Phone"},
  {"id": 2, "name": "Phone"}
]
```
Output:
```csv
id,name,price,stock,category
2,Phone,800,15,electronics
```

## Purpose

This project demonstrates real-world data cleaning techniques such as filtering, deduplication, and data transformation.

## How to run

```bash
python data_cleaning.py
```
