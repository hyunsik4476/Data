# 두 개의 데이터 병합하기
import pandas as pd
import numpy as np

CCTV_Seoul = pd.read_csv('../../data/01. CCTV_in_Seoul.csv')
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)

a = CCTV_Seoul.sort_values(by='소계', ascending=True)

CCTV_Seoul['증가율'] = (CCTV_Seoul['2014년'] + CCTV_Seoul['2015년'] 
+ CCTV_Seoul['2016년']) / CCTV_Seoul['2013년도 이전'] * 100
b = CCTV_Seoul.sort_values(by='증가율', ascending=False)

pop_Seoul = pd.read_excel('../../data/01. population_in_Seoul.xls', header=2, usecols='B, D, G, J, N')
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', pop_Seoul.columns[1] : '인구수', pop_Seoul.columns[2] : '한국인', 
pop_Seoul.columns[3] : '외국인', pop_Seoul.columns[4] : '고령자'}, inplace=True)
pop_Seoul.drop([0], inplace=True)

pop_Seoul['구별'].unique()
c = pop_Seoul[pop_Seoul['구별'].isnull()]
pop_Seoul.drop(c.index, inplace=True)

pop_Seoul['외국인비율'] = pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul['고령자비율'] = pop_Seoul['고령자']/pop_Seoul['인구수']*100

# 공통 컬럼인 '구별'을 기준으로 합치기
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
data_result.drop(['2013년도 이전', '2014년', '2015년', '2016년'], axis=1, inplace=True)
data_result.set_index('구별', inplace=True)
print(data_result[['외국인비율', '소계']].corr())
print(data_result.head())