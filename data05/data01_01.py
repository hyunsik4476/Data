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
print(population)