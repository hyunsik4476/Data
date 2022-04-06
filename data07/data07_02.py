import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet
from datetime import datetime

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

pinkwink_web = pd.read_csv('../../data/08. PinkWink Web Traffic.csv', encoding = 'UTF-8', thousands = ',', names = ['date', 'hit'], index_col = 0)
pinkwink_web = pinkwink_web[pinkwink_web['hit'].notnull()]

df = pd.DataFrame({'ds': pinkwink_web.index, 'y': pinkwink_web['hit']})
df.reset_index(inplace = True)
df['ds'] = pd.to_datetime(df['ds'], format = '%y. %m. %d.')
df.drop(['date'], axis = 1, inplace = True)

# 연 단위의 주기성을 갖는다는 정보
m = Prophet(yearly_seasonality=10)
m.fit(df)

# 앞으로 60일간의 정보에 대한 데이터프레임 만들기
future = m.make_future_dataframe(periods = 60)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
m.plot(forecast)
m.plot_components(forecast)
plt.legend()
plt.show()