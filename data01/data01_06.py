# 두 개의 데이터 병합하기
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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
    print('Unknown system... sorry~~~~') 
#==========================================#

CCTV_Seoul = pd.read_csv('../data/01. CCTV_in_Seoul.csv')
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)

a = CCTV_Seoul.sort_values(by='소계', ascending=True)

CCTV_Seoul['증가율'] = (CCTV_Seoul['2014년'] + CCTV_Seoul['2015년'] 
+ CCTV_Seoul['2016년']) / CCTV_Seoul['2013년도 이전'] * 100
b = CCTV_Seoul.sort_values(by='증가율', ascending=False)

pop_Seoul = pd.read_excel('../data/01. population_in_Seoul.xls', header=2, usecols='B, D, G, J, N')
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', pop_Seoul.columns[1] : '인구수', pop_Seoul.columns[2] : '한국인', 
pop_Seoul.columns[3] : '외국인', pop_Seoul.columns[4] : '고령자'}, inplace=True)
pop_Seoul.drop([0], inplace=True)

pop_Seoul['구별'].unique()
c = pop_Seoul[pop_Seoul['구별'].isnull()]
pop_Seoul.drop(c.index, inplace=True)

pop_Seoul['외국인비율'] = pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul['고령자비율'] = pop_Seoul['고령자']/pop_Seoul['인구수']*100

data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
data_result.drop(['2013년도 이전', '2014년', '2015년', '2016년'], axis=1, inplace=True)
data_result.set_index('구별', inplace=True)

# 시각화하기
# data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))

# 인구 대비 비교해보기
data_result['CCTV 비율'] = data_result['소계'] / data_result['인구수'] * 100
# data_result['CCTV 비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))


# 데이터 가공하기(numpy)
fp = np.polyfit(data_result['인구수'], data_result['소계'], 1)
f1 = np.poly1d(fp)
fx = np.linspace(100000, 700000, 100)

# 오차에 대한 분석
data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))
df_sort = data_result.sort_values(by='오차', ascending=False)


# scattor 함수 써보기
plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'], data_result['소계'], c=data_result['오차'], s = 50) # s = 50 : 마커 사이즈
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n], df_sort.index[n], fontsize=10)

plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.colorbar()

# plt.plot(
#     '인구수',
#     '소계',
#     data = data_result,
#     markersize = 50,
#     linestyle= 'none'
# )

# data_result.plot(x = '인구수', y = '소계', kind='scatter', grid=True, figsize=(10,10))


plt.show()