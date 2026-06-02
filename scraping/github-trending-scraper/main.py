
import csv, requests
from bs4 import BeautifulSoup
import re

FILENAME = "github_trending.csv"

data = [["Name","Description","Language","Stars","Stars_Today","links","forks"]]
url = 'https://github.com/trending'
response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

hub = soup.find_all("article", class_="Box-row")

for repo in hub:
    name = repo.find("span", class_="text-normal").text.strip()
    names = name.replace("/", "")
    element = repo.find("p", class_="col-9 color-fg-muted my-1 tmp-pr-4")
    if element:
        description = element.text.strip()
    else:
        description = ("N/A")
    language = repo.find("span", itemprop="programmingLanguage").text.strip()
    stars = repo.find("a", class_="tmp-mr-3 Link Link--muted d-inline-block").text.strip()
    stars_today = repo.find_all("span")
    for todd in stars_today:
        if "stars today" in todd.text:
            today = todd.text.strip()
            star_today = re.sub(r'\D', '', today)
    links = repo.find("h2").find("a")["href"]
    aclink = f"https://github.com/{links}"
    forks = repo.find_all("a")
    for forg in forks:
        if "forks" in forg["href"]:
            fork = forg["href"]
            acfork = f"https://github.com{fork}"
    # fork
    data.append([names,description,language,stars,star_today,aclink,acfork])
    
with open(FILENAME, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)


