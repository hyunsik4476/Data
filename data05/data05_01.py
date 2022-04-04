import pandas as pd
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

population = pd.read_excel('../../data/05. population_raw_data.xlsx', header = 1)
# fillna : 결측값 (None, NaN 채우기) fillna(0)으로 특정 값으로
# method = 'ffill'/'pad' 로 앞의 값으로, 'bfill'/'backfill' 로 뒤의 값으로
population.fillna(method = 'pad', inplace = True)

population.rename(columns = {'행정구역(동읍면)별(1)':'광역시도', '행정구역(동읍면)별(2)':'시도', '계':'인구수'}, inplace = True)

population = population[population['시도'] != '소계']

# 얕은복사에 의한 워닝 무시
population.is_copy = False

population.rename(columns = {'항목': '구분'}, inplace = True)
population.loc[population['구분'] == '총인구수 (명)', '구분'] = '합계'
population.loc[population['구분'] == '남자인구수 (명)', '구분'] = '남자'
population.loc[population['구분'] == '여자인구수 (명)', '구분'] = '여자'


# 인구 소멸 위기 지역 계산
population['20-39세'] = population['20 - 24세'] + population['25 - 29세'] + population['30 - 34세'] + population['35 - 39세']
population['65세이상'] = population['65 - 69세'] + population['70 - 74세'] + population['75 - 79세'] + population['80 - 84세'] + population['85 - 89세'] + population['90 - 94세'] + population['95 - 99세'] + population['100+']
pop = pd.pivot_table(population, index = ['광역시도', '시도'], columns = ['구분'], values = ['인구수', '20-39세', '65세이상'])
pop['소멸비율'] = pop['20-39세', '여자'] / (pop['65세이상', '합계'] / 2)
pop['소멸위기지역'] = pop['소멸비율'] < 1.0

# 인덱스 통합
pop.reset_index(inplace=True)

# 컬럼 통합
tmp_columns = [pop.columns.get_level_values(0)[n] + pop.columns.get_level_values(1)[n] for n in range(0, len(pop.columns.get_level_values(0)))]
pop.columns = tmp_columns

pop.to_csv('./population.csv', sep = ',', encoding = 'UTF-8')
print(pop)