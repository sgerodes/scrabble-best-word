import requests
from bs4 import BeautifulSoup
from lxml import etree



BASE_URL = 'http://rus-yaz.niv.ru'
MAIN_URL = BASE_URL + '/doc/dictionary/noun/index.htm'


xpath_main = '/html/body/div[2]/a'
xpath_word = r'//a[contains(@class, "t")][contains(@href, "fc")]'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
page = requests.get(MAIN_URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
dom = etree.HTML(str(soup))

with open('vocab/rus-yaz_niv_ru/words.txt', 'w+') as f:
    for elem in dom.xpath(xpath_main):
        sub_url = elem.attrib['href']
        letter_page_url = BASE_URL + sub_url

        print('fetching: ' + letter_page_url)
        page = requests.get(letter_page_url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        dom = etree.HTML(str(soup))
        for elem in dom.xpath(xpath_word):
            #print(elem.text)
            f.write(elem.text + '\n')

