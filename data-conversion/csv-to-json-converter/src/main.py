import argparse

from csv_loader import load_csv
from json_writer import save_json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    return parser.parse_args()

def main():

    args = parse_args()
    rows = load_csv(args.input_file)

    if rows is None:
        return

    if not rows:
        print("Warning: CSV file contains no data rows")
        return
    
    save_json(args.output_file, rows)

    print(f"Rows loaded: {len(rows)}")
    print(f"Rows saved: {len(rows)}")
    print(f"Output file: {args.output_file}")


if __name__ == "__main__":
    main()