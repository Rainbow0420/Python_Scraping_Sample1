import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.tutorialspoint.com/html/index.htm")
bs = BeautifulSoup(response.text, "lxml")
lists = bs.find_all("p")
for ls in lists:
    print(ls.text)
