import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
# print(response.status_code)
# print(response.text[:500])


def fetch_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Bad status code")
        return ""
    else:
        return response.text
    

# print(html[:500])

def get_text_or_empty(parent, selector):
    tag = parent.select_one(selector)
    if tag:
        return tag.get_text(strip=True)
    else:
        return ""

def get_attr_or_empty(parent, selector, attr):
    tag = parent.select_one(selector)

    if tag and tag.has_attr(attr):
        return tag[attr]
    else:
        return ""
    
def extract_product(card):
    title = get_attr_or_empty(card, "h3 a", "title")
    price = get_text_or_empty(card, ".price_color")
    availability = get_text_or_empty(card, ".availability")
    rating_tag = card.select_one("p.star-rating")
    
    if rating_tag and rating_tag.has_attr("class"):
        rating = rating_tag["class"][1]
    else:
        rating = ""


    return {
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating
    }

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select(".product_pod")
    products = []
    for card in cards:
        result = extract_product(card)
        products.append(result)
    
    return products



def save_csv(records, file_path):
    if not records:
        return 
    
    fields = records[0].keys()

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)


html = fetch_html(url)
products = parse_products(html)

save_csv(products, "books.csv")

print(len(products))
print(products[:3])
print("Saved books.csv")