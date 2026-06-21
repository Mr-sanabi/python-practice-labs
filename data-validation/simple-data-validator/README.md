# Simple Data Validator

A small Python CLI tool that reads a CSV file, checks data quality, and saves a validation report as JSON.

## Features

- Reads CSV files from a local path
- Checks for missing values
- Detects duplicate emails
- Validates email format
- Builds a validation summary
- Groups issues by category
- Saves the validation report to JSON
- Uses argparse for input and output file paths
- Handles missing files and CSV files with no data rows

## Tech Stack

- Python
- csv
- json
- argparse
- re

## Usage

```bash
python src/main.py <input_file> <output_file>
```

Example:

```bash
python src/main.py examples/users.csv data/report.json
```

## Example checks

The validator detects:

- Missing values
- Duplicate emails
- Invalid email formats

## Example output summary

```json
{
  "total_rows": 6,
  "missing_value_issues": 2,
  "duplicate_email_issues": 1,
  "invalid_email_issues": 1,
  "total_issues": 4
}
```

## What I practiced

- Reading CSV files with `csv.DictReader`
- Iterating over rows and fields
- Building validation checks
- Detecting missing values
- Detecting duplicate emails with sets
- Validating emails with regex
- Building structured reports
- Saving reports as JSON
- Creating a small CLI tool