import pandas as pd
from glob import glob

# #==========================================#
# import platform

# from matplotlib import font_manager, rc
# plt.rcParams['axes.unicode_minus'] = False

# if platform.system() == 'Darwin':
#     rc('font', family='AppleGothic')
# elif platform.system() == 'Windows':
#     path = "c:/Windows/Fonts/malgun.ttf"
#     font_name = font_manager.FontProperties(fname=path).get_name()
#     rc('font', family=font_name)
# else:
#     print('Unknown system') 
# #==========================================#

stations_files = glob('../../data/지역*.xls')

tmp_raw = []

for file_name in stations_files:
    tmp = pd.read_excel(file_name, header=2)
    tmp_raw.append(tmp)

station_raw = pd.concat(tmp_raw)
# station_raw.info()

stations = pd.DataFrame({'Oil_store':station_raw['상호'], 
                        '주소':station_raw['주소'],
                        '가격':station_raw['휘발유'],
                        '셀프':station_raw['셀프여부'],
                        '상표':station_raw['상표']  })

stations['구'] = [addr.split()[1] for addr in stations['주소']]
stations['구'].unique()
stations.loc[stations['구'] == '서울특별시', '구'] = '성동구'
stations.loc[stations['구'] == '특별시', '구'] = '도봉구'

stations = stations[stations['가격'] != '-']
stations['가격'] = [float(value) for value in stations['가격']]

stations.reset_index(inplace=True)
del stations['index']
stations = stations.loc[:, ['Oil_store', '가격', '상표', '셀프', '주소', '구']]
print(stations.head())
stations.to_csv('./stations.csv', sep = ',', encoding='UTF-8')