from calendar import c
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import json
import folium

from pprint import pprint
# import googlemaps
# gmaps_key = 
# gmaps = googlemaps.Client(key=gmaps_key)
# print(gmaps.geocode('서울중부경찰서', language='ko'))

import platform

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...') 

# 파일 읽어오기
crime_anal_police = pd.read_csv('../../data/02. crime_in_Seoul.csv', thousands=',', encoding='euc-kr')

# 검색을 위해 파일내 경찰서 이름 정보 수정하기
# xx서 -> 서울xx경찰서 로 바꾸기 위해
station_name = []
for name in crime_anal_police['관서명']:
    station_name.append('서울' + str(name[:-1]) + '경찰서')

station_addreess = ['대한민국 서울특별시 중구 을지로동 수표로 27',
 '대한민국 서울특별시 종로구 종로1.2.3.4가동 율곡로 46',
 '대한민국 서울특별시 중구 남대문로5가 한강대로 410',
 '대한민국 서울특별시 서대문구 미근동 통일로 113',
 '대한민국 서울특별시 종로구 종로1.2.3.4가동 창경궁로 112-16',
 '대한민국 서울특별시 용산구 원효로1가 25',
 '대한민국 서울특별시 성북구 삼선동5가 301',
 '대한민국 서울특별시 동대문구 청량리동 약령시로21길 29',
 '대한민국 서울특별시 마포구 아현동 618-1',
 '대한민국 서울특별시 영등포구 당산동3가 2-11',
 '대한민국 서울특별시 성동구 행당1동 왕십리광장로 9',
 '대한민국 서울특별시 동작구 노량진동 72',
 '대한민국 서울특별시 광진구 구의1동 자양로 167',
 '대한민국 서울특별시 은평구 대조동 통일로 757',
 '대한민국 서울특별시 강북구 번1동 415-15',
 '대한민국 서울특별시 관악구 신림동 544',
 '대한민국 서울특별시 중랑구 신내1동 신내역로3길 40-10',
 '대한민국 서울특별시 강남구 대치동 998',
 '대한민국 서울특별시 관악구 봉천동',
 '대한민국 서울특별시 양천구 신월동 화곡로 73',
 '대한민국 서울특별시 강동구 성내1동 성내로 57',
 '대한민국 서울특별시 성북구 종암동 종암로 135',
 '대한민국 서울특별시 구로구 가마산로 235',
 '대한민국 서울특별시 서초구 서초3동 반포대로 179',
 '대한민국 서울특별시 양천구 신정6동 목동동로 99',
 '대한민국 서울특별시 송파구 가락본동 9',
 '대한민국 서울특별시 노원구 하계동 노원로 283',
 '대한민국 서울특별시 서초구 방배2동 방배천로 54',
 '대한민국 서울특별시 은평구 불광2동 연서로 365',
 '대한민국 서울특별시 도봉구 창4동 노해로 403',
 '대한민국 서울특별시 강남구 개포동 개포로 617']
station_lat = [37.5636465,
 37.5755578,
 37.5547584,
 37.5647848,
 37.5718401,
 37.538649,
 37.5897271,
 37.58506149999999,
 37.550814,
 37.5257884,
 37.5617309,
 37.5130685,
 37.542873,
 37.6128611,
 37.6373881,
 37.4814051,
 37.618692,
 37.5094352,
 37.4743789,
 37.5397827,
 37.528511,
 37.6020592,
 37.494931,
 37.4956054,
 37.5165667,
 37.5019065,
 37.6423605,
 37.4815453,
 37.6283597,
 37.6533589,
 37.49349]
station_lng = [126.9895796,
 126.9848674,
 126.9734981,
 126.9667762,
 126.9988562,
 126.966055,
 127.0161318,
 127.0457679,
 126.954028,
 126.901006,
 127.0363806,
 126.9428078,
 127.083821,
 126.9274951,
 127.0273238,
 126.9099508,
 127.1047136,
 127.0669578,
 126.9509748,
 126.8299968,
 127.1268224,
 127.0321577,
 126.886731,
 127.0052504,
 126.8656763,
 127.1271513,
 127.0714027,
 126.9829992,
 126.9287226,
 127.052682,
 127.0772119]

# for name in station_name:
#     tmp = gmaps.geocode(name, language='ko')
#     station_addreess.append(tmp[0].get("formatted_address"))    

#     tmp_loc = tmp[0].get("geometry")
#     station_lat.append(tmp_loc['location']['lat'])
#     station_lng.append(tmp_loc['location']['lng'])

gu_name = []
for name in station_addreess:
    tmp = name.split()
    gu_name.append([gu for gu in tmp if gu[-1] == '구'][0])
crime_anal_police['구별'] = gu_name

# loc 를 사용해 예외사항 처리해주기
crime_anal_police.loc[crime_anal_police['관서명']=='금천서', ['구별']] = '금천구'

# 저장하기
crime_anal_police.to_csv('./crime_in_Seoul_include_gu_name.csv', sep=',', encoding='utf-8')

# 다시 불러오기
crime_anal_raw = pd.read_csv('./crime_in_Seoul_include_gu_name.csv', encoding='utf-8')

# 피봇 테이블 사용하기
crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)

crime_anal['강간검거율'] = crime_anal['강간 검거']/crime_anal['강간 발생']*100
crime_anal['강도검거율'] = crime_anal['강도 검거']/crime_anal['강도 발생']*100
crime_anal['살인검거율'] = crime_anal['살인 검거']/crime_anal['살인 발생']*100
crime_anal['절도검거율'] = crime_anal['절도 검거']/crime_anal['절도 발생']*100
crime_anal['폭력검거율'] = crime_anal['폭력 검거']/crime_anal['폭력 발생']*100

del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

con_list=['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

# loc 으로 특정 조건을 만족하는 index, column 의 값을 수정하기
for column in con_list:
    crime_anal.loc[crime_anal[column]>100, column] = 100

crime_anal.rename(columns={
    '강간 발생': '강간',
    '강도 발생': '강도',
    '살인 발생': '살인',
    '절도 발생': '절도',
    '폭력 발생': '폭력'}, inplace=True)

# 사이킷런 전처리(???)
col = ['강간', '강도', '살인', '절도', '폭력']
x = crime_anal[col].values      # 각 col 의 값만
min_max_scaler = MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x.astype(float))
crime_anal_norm = pd.DataFrame(x_scaled, columns=col, index = crime_anal.index)

col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
crime_anal_norm[col2] = crime_anal[col2]
crime_anal_norm.head()

# 여러 열의 값을 합한 새로운 열 만들기
result_CCTV = pd.read_csv('../../data/01. CCTV_result.csv', encoding='UTF-8', index_col='구별')
crime_anal_norm[['인구수', 'CCTV']] = result_CCTV[['인구수', '소계']]
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis=1)
crime_anal_norm['검거'] = np.sum(crime_anal_norm[col2], axis=1)

# sns.pairplot(crime_anal_norm, vars=['강도', '살인', '폭력'], kind='reg', height=3)
# sns.pairplot(crime_anal_norm, x_vars=['인구수', 'CCTV'], y_vars=['살인검거율','폭력검거율'], kind='reg', height=3)

# 어떤 한 열의 최고값을 100으로 만들기
tmp_max = crime_anal_norm['검거'].max()
crime_anal_norm['검거'] = crime_anal_norm['검거']/tmp_max
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거', ascending=False)

target_col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율', '검거']

crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거', ascending=False)

plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col], annot=True, fmt='f', linewidths=.5, cmap='BuPu')
plt.title('범죄의 검거 비율 (정규화된 검거의 합으로 정렬)')
plt.show()

target_col_2 = ['강간', '강도', '살인', '절도', '폭력', '범죄']
crime_anal_norm['범죄'] = crime_anal_norm['범죄'] /5
crime_anal_norm_sort = crime_anal_norm.sort_values(by='범죄', ascending=False)
plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col_2], annot=True, fmt='f', linewidths=.5, cmap='BuPu')
plt.title('범죄 비율 (정규화된 발생 건수로 정렬)')
plt.show()

crime_anal_norm.to_csv('./02. crime_in_Seoul_final.csv', sep=',', encoding='utf-8')

# 지도 시각화
geo_path = '../../data/02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding = 'utf-8'))

# 데이터 만들기
tmp_criminal = crime_anal_norm['범죄'] /  crime_anal_norm['인구수'] * 1000000

crime_anal_raw['lat'] = station_lat
crime_anal_raw['lng'] = station_lng

col = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
tmp = crime_anal_raw[col] / crime_anal_raw[col].max()
crime_anal_raw['검거'] = np.sum(tmp, axis = 1)


# 지도 만들기
map = folium.Map(location=[37.5502, 126.982], zoom_start=11, 
                 tiles='Stamen Toner')

map.choropleth(geo_data = geo_str,
               data = tmp_criminal,
               columns = [crime_anal.index, tmp_criminal],
               fill_color = 'PuRd', #PuRd, YlGnBu
               key_on = 'feature.id')

for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]], radius = crime_anal_raw['검거'][n]*10, popup=crime_anal_raw['관서명'][n], color = '#3186cc', fill_color = '#3186cc').add_to(map)

map.save('./map.html')
