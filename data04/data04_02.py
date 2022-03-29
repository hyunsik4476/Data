import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

stations = pd.read_csv('./stations.csv')
stations.drop(['Unnamed: 0'], axis = 1, inplace = True)
print(stations.head())

stations.boxplot(column = '가격', by = '셀프', figsize = (12, 8))
plt.figure(figsize = (12, 8))
sns.boxplot(x = '상표', y = '가격', data = stations, palette = 'Set3')
sns.swarmplot(x = '상표', y = '가격', hue = '셀프', data = stations, color = '.6')
plt.show()