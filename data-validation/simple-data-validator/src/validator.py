import re

def find_missing_values(rows):
    issues = []

    for row_number, row in enumerate(rows, start=1):
        for field, value in row.items():
            if value is None or value.strip() == "":
                issue = {
                    "row_number": row_number,
                    "field": field,
                    "issue": "missing_value"
                }

                issues.append(issue)
    
    return issues


def find_duplicate_emails(rows):
    seen_emails = set()
    issues = []
    
    for row_number, row in enumerate(rows, start=1):
        email = row.get("email", "").strip().lower()

        if email == "":
            continue

        if email in seen_emails:
            issue = {
                "row_number": row_number,
                "field": "email",
                "value": email,
                "issue": "duplicate_email"
            }
            issues.append(issue)
        else:
            seen_emails.add(email)

    
    return issues


def find_invalid_emails(rows):
    issues = []
    for row_number, row in enumerate(rows , start=1):
        email = row.get ("email", "").strip().lower()

        if email == "":
            continue

        email_regex = re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email)

        if not email_regex:
            issue = {
                "row_number": row_number,
                "field": "email",
                "value": email,
                "issue": "invalid_email"
            }
            issues.append(issue)

    return issues


def validate_rows(rows):
    missing_values = find_missing_values(rows)
    duplicate_emails = find_duplicate_emails(rows)
    invalid_emails = find_invalid_emails(rows)
    total_issues = missing_values + duplicate_emails + invalid_emails

    report = {
        "summary": {
            "total_rows": len(rows),
            "missing_value_issues": len(missing_values),
            "duplicate_email_issues":len(duplicate_emails),
            "invalid_email_issues": len(invalid_emails),
            "total_issues": len(total_issues)
        },
        "issues": {
            "missing_values": missing_values,
            "duplicate_emails": duplicate_emails,
            "invalid_emails": invalid_emails
        }
    }

    return report