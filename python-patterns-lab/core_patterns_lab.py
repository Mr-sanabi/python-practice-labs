# =========================
# Gate 2 — return
# =========================


def clean_price(raw_price):
    cleaned = raw_price.replace("$", "")
    price = float(cleaned)
    return price

# price = clean_price("$29.99")
# print(price)
# print(price + 10)

def apply_discount(price, percent):
    discount = price * percent / 100
    final_price = price - discount
    return final_price

discounted_price = apply_discount(113, 20)
# print(discounted_price)

raw_price = "$50.00"

price = clean_price(raw_price)
final_price = apply_discount(price, 10)

# print(final_price)


# =========================
# Gate 3 — list building
# =========================

raw_products = [
    ["Black Shirt", "$29.99", "SKU001"],
    ["White Shirt", "$24.99", "SKU002"],
    ["Blue Hoodie", "$49.99", "SKU003"],
]


def build_product_records(raw_products):
    result = []

    for product in raw_products:
        title = product[0]
        price = product[1]
        sku = product[2]

        record = {
            "title": title,
            "price": price,
            "sku": sku,
        }

        result.append(record)

    return result

products = build_product_records(raw_products)
# print(product)


def build_simple_report(products):
    lines = []

    lines.append("# Product Report")
    lines.append("")
    lines.append(f"Total products: {len(products)}")
    lines.append("")

    for product in products:
        lines.append(f"- {product['title']} - {product['price']}")

    return "\n".join(lines)

report = build_simple_report(products)
# print(report)


# =========================
# Gate 4 — enumerate
# =========================


def build_numbered_report(products):
    lines = []

    lines.append("# Numbered Product Report")
    lines.append("")

    for index, product in enumerate(products, start=1):
        lines.append(f"## Product {index}")
        lines.append(f"Title: {product['title']}")
        lines.append(f"Price: {product['price']}")
        lines.append(f"SKU: {product['sku']}")

    return "\n".join(lines)

numbered_report = build_numbered_report(products)
# print(numbered_report)


# =========================
# Gate 5 — nested loops
# =========================


def build_detailed_report(products):
    lines = []

    lines.append("# Datailed Product Report")
    lines.append("")

    for index, product in enumerate(products, start=1):
        lines.append(f"## Product {index}")
        lines.append("")

        for key, value in product.items():
            lines.append(f"- {key}: {value}")

        lines.append("")

    return "\n".join(lines)

detailed_report = build_detailed_report(products)
print(detailed_report)