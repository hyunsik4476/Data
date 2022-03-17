import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
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

df = pd.read_csv('./03. best_sandwiches_list_chicago.csv', index_col = 0)

price = []
address = []
for i in df.index:
    html = urlopen(df['URL'][i])
    soup = BeautifulSoup(html, 'html.parser')

    tmp_str = soup.find('p', 'addy').get_text()

    price.append(tmp_str.split()[0][:-1])
    address.append(' '.join(tmp_str.split()[1:-2]))

df['Price'] = price
df['Address'] = address
df = df.loc[:, ['Rank', 'Cafe', 'Menu', 'Price', 'Address']]
df.set_index('Rank', inplace = True)
df.to_csv('./03. bslc2.csv', sep = ',', encoding = 'UTF-8')