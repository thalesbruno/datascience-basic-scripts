# sample.py
from bs4 import BeautifulSoup
import requests

url = "https://raw.githubusercontent.com/joelgrus/data/master/getting-data.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')

print(first_paragraph)
