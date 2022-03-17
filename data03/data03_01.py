# 부티풀슾으로 html 문서 분석하기
from bs4 import BeautifulSoup

page = open('./03. test_first.html', 'r').read()
soup = BeautifulSoup(page, 'html.parser')
html = list(soup.children)[2]
body = soup.body

links = soup.find_all('a')
for link in links:
    href = link['href']
    text = link.string
    print(text, '->', href)
