import pandas as pd
import numpy as np

# csv 파일 읽기
CCTV_Seoul = pd.read_csv('../data/01. CCTV_in_Seoul.csv', encoding='utf-8')
CCTV_Seoul.head()
CCTV_Seoul.columns
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
print(CCTV_Seoul.head())
print()

# 엑셀 파일 읽기
pop_Seoul = pd.read_excel('../data/01. population_in_Seoul.xls', header = 2, usecols = 'B, D, G, J, N')
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', pop_Seoul.columns[1] : '인구수', pop_Seoul.columns[2] : '한국인', 
pop_Seoul.columns[3] : '외국인', pop_Seoul.columns[4] : '고령자'}, inplace=True)
print(pop_Seoul.head())
print()

# 시리즈 데이터형
s = pd.Series([1,3,5,7,9])
print(s)

# 데이터프레임 만들기
dates = pd.date_range('20220302', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns=['A', 'B', 'C', 'D'])
print(df.sort_index())
print(df.describe())
print(df[df['A'] > 0])

# 특정 행, 열 수정/ 추가
# df['E'] = [1, 2, 3, 4, 5, 6]
# df.loc[dates[0]] = [1, 2, 3, 4]
# print(df)

# 함수를 적용하기
print(df.apply(np.cumsum))  # 열 기준 누적 합
print(df.apply(lambda x: x + 1))    # 람다함수 사용 가능