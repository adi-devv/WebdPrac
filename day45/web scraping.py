from bs4 import BeautifulSoup
import requests

resp = requests.get("https://en.wikipedia.org/wiki/India")

soup = BeautifulSoup(resp.text, 'html.parser')
heading = soup.find_all(name='span', class_="mw-headline")

for item in heading:
    print(item.string, end=" ")
    t2 = item.parent.find_next_sibling()
    div = t2.find_next_sibling().find('a')

    if div:
        print(div.string, div.get('href'))
    else:
        print()
