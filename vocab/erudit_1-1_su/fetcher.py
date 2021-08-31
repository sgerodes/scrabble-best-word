import requests
from bs4 import BeautifulSoup
from lxml import etree

FETCH_URL = 'https://erudit.1-1.su/?chars=***************&mask=***************&position=1&left=15&right=15&sorting=2'



# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
# }
# page = requests.get(FETCH_URL, headers=headers)
page = requests.get(FETCH_URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
#dom = etree.HTML(str(soup))