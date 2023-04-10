import requests
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
bs = BeautifulSoup(response.text, "lxml")
lists = bs.find_all("p")
for ls in lists:
    print(ls.text)
