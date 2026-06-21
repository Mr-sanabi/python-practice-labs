import argparse

from csv_loader import load_csv
from report_writer import save_report
from validator import validate_rows


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

    report = validate_rows(rows)
    save_report(args.output_file, report)

    print(report["summary"])
    print(f"Report saved: {args.output_file}")


if __name__ == "__main__":
    main()