import pandas as pd
import numpy as np

CCTV_Seoul = pd.read_csv('../../data/01. CCTV_in_Seoul.csv')
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
# 1. CCTV의 갯수로 정렬하기
a = CCTV_Seoul.sort_values(by='소계', ascending=True)

# 2. CCTV의 증가율 확인해보기
CCTV_Seoul['증가율'] = (CCTV_Seoul['2014년'] + CCTV_Seoul['2015년'] 
+ CCTV_Seoul['2016년']) / CCTV_Seoul['2013년도 이전'] * 100
b = CCTV_Seoul.sort_values(by='증가율', ascending=False)

# 3. 엑셀파일로 인구 수 받아오기
pop_Seoul = pd.read_excel('../../data/01. population_in_Seoul.xls', header=2, usecols='B, D, G, J, N')
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', pop_Seoul.columns[1] : '인구수', pop_Seoul.columns[2] : '한국인', 
pop_Seoul.columns[3] : '외국인', pop_Seoul.columns[4] : '고령자'}, inplace=True)

# 4. 필요없는 행(합계) 삭제하기
pop_Seoul.drop([0], inplace=True)

# 5. 반복되는 행 조사하는 방법
pop_Seoul['구별'].unique()

# 5.5. NaN 데이터 찾는 방법, 삭제하는 방법
c = pop_Seoul[pop_Seoul['구별'].isnull()]
pop_Seoul.drop(c.index, inplace=True)
pop_Seoul['외국인비율'] = pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul['고령자비율'] = pop_Seoul['고령자']/pop_Seoul['인구수']*100
print(pop_Seoul)