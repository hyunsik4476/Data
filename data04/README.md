# 04 셀프주유소 가격 분석

## 여러 파일 한번에 불러와 합치기

```python
stations_files = glob('../../data/지역*.xls')

tmp_raw = []

for file_name in stations_files:
    tmp = pd.read_excel(file_name, header=2)
    tmp_raw.append(tmp)

station_raw = pd.concat(tmp_raw)
```

* glob 으로 불러온 여러 xls 파일을 리스트에 저장하고 pandas 의 concat 함수로 하나로 합침



## 데이터프레임

### 생성 & 예외처리

```python
stations = pd.DataFrame({'Oil_store':station_raw['상호'], 
                        '주소':station_raw['주소'],
                        '가격':station_raw['휘발유'],
                        '셀프':station_raw['셀프여부'],
                        '상표':station_raw['상표']  })

stations['구'] = [addr.split()[1] for addr in stations['주소']]
stations['구'].unique()
stations.loc[stations['구'] == '서울특별시', '구'] = '성동구'
stations.loc[stations['구'] == '특별시', '구'] = '도봉구'
```

* 원하는 정보 뽑아서 데이터프레임으로 변환
* 예외처리 1 : 구 이름이 잘못 입력된 경우
* loc의 경우 [인덱스, 콜럼] 으로 지정

```python
stations = stations[stations['가격'] != '-']
stations['가격'] = [float(value) for value in stations['가격']]
```

* 예외처리 2 : 입력이 - 인 행이 있어 숫자형으로 처리가 안됨
* 해당 행들을 삭제시키고 float 변환



### 인덱스 관련

```python
stations.reset_index(inplace=True)
del stations['index']
stations = stations.loc[:, ['Oil_store', '가격', '상표', '셀프', '주소', '구']]
stations.info()
```

* 여러 파일을 합쳤을 때 index가 겹칠 수 있으므로 reset_index를 활용해 다시 인덱스 번호 매김
* 인덱스 열이 하나 더 생성되기 때문에 del 로 삭제
* loc 파일로 원하는 열을 원하는 순서로 정렬



## 플롯

```python
stations = pd.read_csv('./stations.csv')
stations.drop(['Unnamed: 0'], axis = 1, inplace = True)
print(stations.head())
```

* 앞에서 저장한 csv 파일을 불렀을 때 원하지 않는 콜럼이 생성돼 삭제
* read_csv 의 index_col = 0 옵션을 빼먹으면 이렇게 된다

```python
stations.boxplot(column = '가격', by = '셀프', figsize = (12, 8))
plt.figure(figsize = (12, 8))
sns.boxplot(x = '상표', y = '가격', data = stations, palette = 'Set3')
sns.swarmplot(x = '상표', y = '가격', hue = '셀프', data = stations, color = '.6')
plt.show()
```

* hue를 이용해 한 컬럼에서 내용 나누는게 가능



## 추가

* pivot_table 기능과 aggfunc 을 이용해 특정 구의 기름 가격만 포함하는 테이블을 만들 수 있음