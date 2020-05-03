# house_of_representatives.py
from bs4 import BeautifulSoup
from typing import Dict, Set
import requests
import re

url = "https://www.house.gov/representatives"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]

# getting only urls that starts with 'http://' or 'https://' and ends with
# '.house.gov' or '.house.gov/'
regex = r"^https?://.*\.house\.gov/?$"

good_urls = [url for url in all_urls if re.match(regex, url)]

# removing duplicates
unique_good_urls = list(set(good_urls))

print(f"{len(all_urls)} urls")
print(f"{len(good_urls)} good urls")
print(f"{len(unique_good_urls)} unique good urls")

print(f"searching in all congresspeople press releases for 'data' mentions...")

# getting press releases links from each house representative page
press_releases: Dict[str, Set[str]] = {}

for house_url in unique_good_urls:
    html = requests.get(house_url).text
    soup = BeautifulSoup(html, 'html5lib')
    pr_links_original = {a['href']
                         for a in soup('a')
                         if 'press release' in a.text.lower()}

    # handling relative links
    regex = r"^https?"
    pr_links = {link
                if re.match(regex, link)
                else house_url+link
                for link in pr_links_original}

    # discarding empty sets
    if pr_links:
        # print(f"{house_url}: {pr_links}")
        press_releases[house_url] = pr_links


def paragraph_mentions(text: str, keyword: str) -> bool:
    """
    Returns True if a <p> inside the text mentions {keyword}
    """
    soup = BeautifulSoup(text, 'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]

    return any(keyword.lower() in paragraph.lower() for paragraph in paragraphs)


for house_url, pr_links in press_releases.items():
    for pr_link in pr_links:
        url = f"{pr_link}"
        text = requests.get(url).text

        if paragraph_mentions(text, 'data'):
            print(f"{house_url} has mentioned 'data")
