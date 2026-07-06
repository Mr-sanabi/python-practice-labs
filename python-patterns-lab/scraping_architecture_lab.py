# Scraping Architecture Lab
# Goal: practice BeautifulSoup parsing architecture on local HTML.

from bs4 import BeautifulSoup
import csv

# =========================
# Gate 2 — BeautifulSoup object
# =========================

html = """
<html>
  <body>
    <div class="product-card">
      <h2 class="title">Black Shirt</h2>
      <p class="price">$29.99</p>
      <span class="availability">In stock</span>
    </div>

    <div class="product-card">
      <h2 class="title">White Shirt</h2>
      <p class="price">$24.99</p>
      <span class="availability">Out of stock</span>
    </div>

    <div class="product-card">
      <h2 class="title">Blue Hoodie</h2>
      <p class="price">$49.00</p>
      <span class="availability">In stock</span>
    </div>

    <div class="product-card">
      <h2 class="title">Red Cap</h2>
      <span class="availability">In stock</span>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())


# =========================
# Gate 3 — find / find_all
# =========================


first_card = soup.find("div", class_="product-card")

cards = soup.find_all("div", class_="product-card")
# print(len(cards))

title_tag = first_card.find("h2", class_="title")
# print(title_tag)
# print(title_tag.get_text(strip=True))

price_tag = first_card.find("p", class_=("price"))
# print(price_tag.get_text(strip=True))


# =========================
# Gate 4 — select / select_one
# =========================


first_card_css = soup.select_one(".product-card")
# print(first_card_css)

cards_css = soup.select(".product-card")
# print(len(cards_css))

title_tag = first_card_css.select_one(".title")
# print(title_tag.get_text(strip=True))

price_tag = first_card_css.select_one(".price")
# print(price_tag.get_text(strip=True))


# =========================
# Gate 5 — card extraction function
# =========================


def extract_product(card):
    title_tag = card.select_one(".title")
    price_tag = card.select_one(".price")
    availability_tag = card.select_one(".availability")

    title = title_tag.get_text(strip=True)
    price = price_tag.get_text(strip=True)
    availability = availability_tag.get_text(strip=True)

    return {
        "title": title,
        "price": price,
        "availability": availability
    }

# first_product = extract_product(first_card_css)
# print(first_product)


# =========================
# Gate 6 — multiple cards to list[dict]
# =========================


# products = []

# for card in cards_css:
#     product = extract_product(card)
#     products.append(product)

# print(products)


# =========================
# Gate 7 — safe extraction
# =========================


def get_text_or_empty(card, selector):
    
    tag = card.select_one(selector)

    if tag:
        return tag.get_text(strip=True)
    
    return ""

def extract_product(card):

    title = get_text_or_empty(card, ".title")
    price = get_text_or_empty(card, ".price")
    availability = get_text_or_empty(card, ".availability")

    return {
        "title": title,
        "price": price,
        "availability": availability
    }

products = []

for card in cards_css:
    product = extract_product(card)
    products.append(product)

# print(products)

# =========================
# Gate 8 — CSV output
# =========================


def save_output(filename, rows):
    if not rows:
        return
    
    fields = rows[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


save_output("products.csv",products)