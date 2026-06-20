# Playwright Basics — Dynamic Page Extractor

A small Python practice project for learning Playwright basics.

The script opens a JavaScript-rendered page, extracts quote text and authors, converts the extracted data into rows, and saves the result to a CSV file.

## Features

- Opens a page with Playwright Chromium
- Handles JavaScript-rendered content
- Extracts quote cards from the page
- Extracts quote text and author names
- Converts extracted data into dictionaries
- Exports the result to CSV
- Uses argparse for output file path

## Tech Stack

- Python
- Playwright
- argparse
- csv

## Usage

```bash
python src/main.py <output_file>
```

Example:

```bash
python src/main.py data/quotes.csv
```

## Output columns

```text
quote, author
```

## What I practiced

- Opening a browser with Playwright
- Using `page.goto()`
- Using `locator()`
- Extracting visible text
- Working with repeated page cards
- Saving scraped data to CSV