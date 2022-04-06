import pandas as pd
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
ex = pd.read_csv('../../data/07. example_wp_peyton_manning.csv')
time = pd.date_range(start = '2014-01-01', periods = len(ex['y']))
df = pd.DataFrame({'ds': time, 'y': ex['y']})
df.reset_index(inplace = True)
plt.figure(figsize = (10, 6))
plt.scatter(time, ex['y'], s = 1)

m = Prophet(yearly_seasonality = True)
m.fit(df)
future = m.make_future_dataframe(periods = 60)
forecast = m.predict(future)
m.plot(forecast)
plt.show()