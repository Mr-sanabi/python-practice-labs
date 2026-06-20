import argparse
from playwright.sync_api import sync_playwright
from storage import save_csv


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file")
    return parser.parse_args()


def main():
    args = parse_args()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://quotes.toscrape.com/js/")

        title = page.title()
        print(title)

        quote_text = page.locator(".text")
        texts = quote_text.all_text_contents()

        quote_cards = page.locator(".quote")
        count = quote_cards.count()
        print(count)
        rows = []
        for i in range(count):
            quote_card = quote_cards.nth(i)
            text = quote_card.locator(".text").text_content()
            author = quote_card.locator(".author").text_content()
        
            row = {
                "quote": text,
                "author": author,
            }
        
            rows.append(row)
        
        print(f"Rows collected: {len(rows)}")
        print(rows[0])
        save_csv(args.output_file, rows)
        browser.close
    
if __name__ == "__main__":
    main()