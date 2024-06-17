from bs4 import BeautifulSoup
with open('website.html', 'r', encoding='utf-8') as f:
    contents = f.read()


soup = BeautifulSoup(contents, 'html.parser')

alla = soup.find_all(name='a')

for a in alla:
    print(a.get('href'), a.string)

url = soup.select(selector=".heading")
print(url)