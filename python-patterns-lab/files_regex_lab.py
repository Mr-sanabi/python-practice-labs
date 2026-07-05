import re


# Files + Regex Lab
# Goal: practice reading/writing text files and extracting data with regex.


# =========================
# Gate 2 — file write/read basics
# =========================


def write_text_file(file_path, text):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

# write_text_file("sample.txt", "Hello from Python file writing!")


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content =  file.read()

    return content

# content = read_text_file("sample.txt")
# print(content)


def append_text_file(file_path, text):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text)


append_text_file("sample.txt", "\nSecond line added with append")


# =========================
# Gate 3 — regex basics
# =========================


messy_text = """
Contact us at hello@example.com or support@test.org.
Product price: $29.99
Discount price: $19.50
Website: https://example.com/products/123
Order ID: ORD-2026-001
"""


email_match = re.search(r"\w+@\w+\.\w+", messy_text)

# if email_match:
#     print(email_match.group())
# else:
#     print("No email found")


emails = re.findall(r"\w+@\w+\.\w+", messy_text)
# print(emails)


prices = re.findall(r"\$\d+\.\d+", messy_text)
# print(prices)


urls = re.findall(r"https?://\S+", messy_text)
# print(urls)


# =========================
# Gate 4 — regex extraction functions
# =========================


def extract_emails(text):
    emails = re.findall(r"\w+@\w+\.\w+", text)
    return emails


def extract_prices(text):
    prices = re.findall(r"\$\d+\.\d+", text)
    return prices


def extract_urls(text):
    urls = re.findall(r"https?://\S+", text)
    return urls


# emails = extract_emails(messy_text)
# prices = extract_prices(messy_text)
# urls = extract_urls(messy_text)

# empty_text = "No useful data here."

# print("Emails:", empty_text)
# print("Prices:", empty_text)
# print("URLs:", empty_text)

text = read_text_file("messy_text.txt")
# print(text)

emails = extract_emails(text)
prices = extract_prices(text)
urls = extract_urls(text)

print("Email:", emails)
print("Prices:", prices)
print("URLs:", urls)


def build_extraction_report(emails, prices, urls):
    lines = []
    lines.append("# Extraction Report")
    lines.append("")
    lines.append("## Emails")
    
    for email in emails:
        lines.append(f"- {email}")
    lines.append("")
    lines.append("## Prices")

    for price in prices:
        lines.append(f"- {price}")
    lines.append("")
    lines.append("## URLs")

    for url in urls:
        lines.append(f"- {url}")

    return "\n".join(lines)

report = build_extraction_report(emails, prices, urls)
write_text_file("extracted_report.md", report)
