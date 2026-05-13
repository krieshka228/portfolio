import requests
from openpyxl import Workbook
import re
from bs4 import BeautifulSoup
wb = Workbook()
ws = wb.active
arr = ['Автор','Цитата','Теги']
clean = []
url = "https://quotes.toscrape.com"
while url:
    response = requests.get(url)
    tree = response.content
    soup = BeautifulSoup(tree,'lxml')
    data_text = soup.find_all('div',attrs = {'class':'quote'})


    for quote in data_text:
        text = quote.find('span',class_='text').get_text()
        autor = quote.find('small',class_='author').get_text()
        tags_div = quote.find('div', class_='tags')
        tags = []
        if tags_div:
            tag_links = tags_div.find_all('a', class_='tag')
            tags = [tag.get_text() for tag in tag_links]
        clean.append({'autor':autor,'text':text,'tags':tags})
    next_button = soup.find('li',attrs = {'class':'next'})
    if next_button:
        next_page_relative = next_button.find('a')['href']
        url = f"https://quotes.toscrape.com/{next_page_relative}"
    else:
        break
ws.append(arr)
for quote in clean:
    ws.append([quote['autor'],quote['text'],', '.join(quote['tags'])])
wb.save('quotes.xlsx')