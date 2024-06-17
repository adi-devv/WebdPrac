import requests
from bs4 import BeautifulSoup

resp = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(resp.text, 'html.parser')
titles = [h3.string for h3 in soup.select('div.article-title-description__text h3')]
titles.reverse()

with open("movies.txt", 'w', encoding='utf-8') as f:
    f.write('\n'.join(titles)+'\n')
