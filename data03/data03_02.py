import re
from bs4 import BeautifulSoup
import pandas as pd

# from urllib.request import urlopen
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError

# 403 forbidden 해결용
def urlopen(url):
    try:
        headers = {'User-Agent' : 'Chrome/66.0.3359.181'}
        req = urllib.request.Request(url, headers = headers)
        html = urllib.request.urlopen(req)
    
    except HTTPError as e:
        err = e.read()
        code = e.getcode()

    source = html.read()

    return source

# https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/
url_base = 'https://www.chicagomag.com/'
url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
url = 'https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

list_soup = soup.find_all('div', 'sammy')

# html 태그에서 필요한 정보 추출하기
rank = []
main_menu = []
cafe_name = []
url_add = []

for item in list_soup:
    rank.append(item.find(class_ = 'sammyRank').get_text())

    tmp_str = item.find(class_ = 'sammyListing').get_text()
    main_menu.append(re.split(('\n|\r\n'), tmp_str)[0])
    cafe_name.append(re.split(('\n|\r\n'), tmp_str)[1])

    url_add.append(urllib.parse.urljoin(url_base, item.find('a')['href']))

data = {'Rank': rank, 'Menu': main_menu, 'Cafe': cafe_name, 'URL': url_add}
df = pd.DataFrame(data, columns=['Rank', 'Cafe', 'Menu', 'URL'])
df.to_csv('./03. best_sandwiches_list_chicago.csv', sep = ',', encoding = 'UTF-8')
print(df.head(5))