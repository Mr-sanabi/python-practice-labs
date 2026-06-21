# CSV to JSON Converter

A small Python CLI tool that reads CSV data, converts rows into JSON objects, and saves the result as a structured JSON file.

## Features

- Reads CSV files from a local path
- Converts CSV rows into a list of dictionaries
- Uses CSV headers as JSON field names
- Exports clean JSON with readable indentation
- Uses argparse for input and output file paths
- Handles missing files and CSV files with no data rows

## Tech Stack

- Python
- csv
- json
- argparse

## Usage

```bash
python src/main.py <input_file> <output_file>
```

Example:

```bash
python src/main.py examples/users.csv data/output.json
```

## Example input

```csv
id,name,email,city,company,active
1,John Miller,john.miller@example.com,Warsaw,Northwind Trading,true
2,Anna Kowalska,anna.kowalska@example.com,Krakow,BlueSoft Analytics,false
```

## Example output

```json
[
  {
    "id": "1",
    "name": "John Miller",
    "email": "john.miller@example.com",
    "city": "Warsaw",
    "company": "Northwind Trading",
    "active": "true"
  }
]
```

## What I practiced

- Reading CSV files with `csv.DictReader`
- Converting CSV rows into dictionaries
- Saving Python data as JSON
- Building a small CLI tool
- Using argparse for command-line arguments
- Basic file and empty-data handling