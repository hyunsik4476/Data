from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.request import urlopen
import urllib
from tqdm import tqdm_notebook
import matplotlib.pyplot as plt

#==========================================#
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system') 
#==========================================#

'''
page = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20170806'

soup = BeautifulSoup(page, 'html.parser')
soup.find_all('div', 'tit5')

date = pd.date_range('2021-5-1', periods = 100, freq = 'D')

movie_date = []
movie_name = []
movie_point = []

for today in tqdm_notebook(date):
    html = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={date}'

    response = urlopen(html.format(date = urllib.parse.quote(today.strftime('%Y%m%d'))))
    soup = BeautifulSoup(response, 'html.parser')

    end = len(soup.find_all('td', 'point'))

    movie_date.extend([today for n in range(0, end)])
    movie_name.extend([soup.find_all('div', 'tit5')[n].a.string for n in range(0, end)])    # 사이트 html 에 제목이 a태그 안에 들어있음
    movie_point.extend([soup.find_all('td', 'point')[n].string for n in range(0, end)])

movie = pd.DataFrame({'date': movie_date, 'name': movie_name, 'point': movie_point})
movie.to_csv('./movie.csv', sep = ',', encoding='UTF-8')
'''

movie = pd.read_csv('./movie.csv', index_col=0)
tmp = movie.query('name == ["중경삼림"]')

# plt.figure(figsize = (12, 8))
# plt.plot(tmp['date'], tmp['point'])
# plt.xticks([n for n in range(0, 101, 10)], rotation=90)   # 파이썬식으로도 잘 됨
# plt.legend()
# plt.grid()
# plt.show()

movie_pivot = pd.pivot_table(movie, index = ['date'], columns = ['name'], values = ['point'])
movie_pivot.columns = movie_pivot.columns.droplevel()   # 왜 안됐는가? .columns 을 안써서 레벨 1인 인덱스에서 드롭레벨을 시도했기 때문
movie_pivot.plot(y = ['중경삼림', '화양연화', '해피 투게더'], figsize = (12, 6))
plt.legend()
plt.grid()
plt.show()
# print(movie_pivot)
