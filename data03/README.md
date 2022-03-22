## ch.3

## BeautifulSoup

### 시작하기: 파싱

> 구문을 해석할 수 있는 단위로 분할해줌

* `variable = BeautifulSoup(<html이 저장된 변수>, 'html.parser')`
* `.prettify()` 를 사용해 html 문서처럼 들여쓰기 된 상태로 보기 가능



### 태그별 분석

* `.children` 으로 해당 태그의 자식 조회 가능
* 즉, 문서 -> html 태그 -> head, body 태그 순으로 조회할 수 있음
* 혹은 `.body` 로 한 번에 원하는 태그 보기 가능



* 접근해야 할 태그를 알 때
  * `.find_all('p')` 로 모든 p태그 리스트 반환
  * `.find('p')` 로 가장 앞의 p 태그 반환
  * `.find('p', class='outer-text')` 처럼 특정 클래스를 갖는 태그도 찾을 수 있음
  * `.next-sibling` 으로 같은 높이의 다음 태그에 접근 가능



### 텍스트에 접근

* `.get_text()` 로 태그 내부의 텍스트만 가지고 올 수 있음

* ```python
  links = soup.find_all('a')
  for link in links:
      href = link['href']
      text = link.string
      print(text, '->', href)
  ```

* 이런 식의 사용도 가능

* `.string` 의 경우 문자열이 없으면 None 을 반환하지만 `.get_text()` 는 유니코드 형식으로 텍스트까지 문자열로 반환하기 때문에 아무 정보도 나오지 않음

  * 하위태그에 텍스트까지 파싱한다면 get_text, 아니라면 string



### 예시

```python
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

list_soup = soup.find_all('div', 'sammy')

# html 태그에서 필요한 정보 추출하기
rank = []
main_menu = []
cafe_name = []
url_add = []

for item in list_soup:
    rank.append(item.find(class_ = 'sammyRank').get_text())

    tmp_str = item.find(class_ = 'sammyListing').get_text()
    main_menu.append(re.split(('\n|\r\n'), tmp_str)[0])
    cafe_name.append(re.split(('\n|\r\n'), tmp_str)[1])

    url_add.append(urllib.parse.urljoin(url_base, item.find('a')['href']))

data = {'Rank': rank, 'Menu': main_menu, 'Cafe': cafe_name, 'URL': url_add}
df = pd.DataFrame(data, columns=['Rank', 'Cafe', 'Menu', 'URL'])
df.to_csv('./03. best_sandwiches_list_chicago.csv', sep = ',', encoding = 'UTF-8')
```



### 오류

* pivot_table 에서 추가로 생기는 레벨의 경우 아무것도 안적으면 인덱스 기준인 듯 하다.
  * ` movie_pivot.columns = movie_pivot.columns.droplevel()` 처럼 써야 콜럼레벨이 지워짐
* `plt.xticks([n for n in range(0, 101, 10)], rotation=90)` 처럼 xlabel 간격을 지정 가능
* `end = len(soup.find_all('td', 'point'))` 파싱할 때, 태그를 몇 개나 찾아야 하는지 모를 경우 이런식으로 사용 가능