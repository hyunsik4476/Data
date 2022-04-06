import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import pandas_datareader.data as web
import numpy as np

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

# 모델의 적합성 확인을 위해 참 값과 비교해 에러를 계산하는 함수
def error(f, x, y):
    return np.sqrt(np.mean((f(x) - y)**2))


pinkwink_web = pd.read_csv('../../data/08. PinkWink Web Traffic.csv', encoding = 'UTF-8', thousands = ',', names = ['date', 'hit'], index_col = 0)
pinkwink_web = pinkwink_web[pinkwink_web['hit'].notnull()]

# arange 를 통해 구간을 스텝 단위로 나눈 리스트 받기
time = np.arange(0, len(pinkwink_web))
traffic = pinkwink_web['hit'].values
fx = np.linspace(0, time[-1], 1000)

fp1 = np.polyfit(time, traffic, 1)
f1 = np.poly1d(fp1)

f2p = np.polyfit(time, traffic, 2)
f2 = np.poly1d(f2p)

f3p = np.polyfit(time, traffic, 3)
f3 = np.poly1d(f3p)

f15p = np.polyfit(time, traffic, 15)
f15 = np.poly1d(f15p)

plt.figure(figsize = (10, 6))
plt.scatter(time, traffic, s = 10)
plt.plot(fx, f1(fx), lw = 4, label = 'f1')
plt.plot(fx, f2(fx), lw = 4, label = 'f2')
plt.plot(fx, f3(fx), lw = 4, label = 'f3')
plt.plot(fx, f15(fx), lw = 4, label = 'f15')
plt.grid(True, linestyle = '-', color = '0.75')

plt.show()
# print(pinkwink_web.head())