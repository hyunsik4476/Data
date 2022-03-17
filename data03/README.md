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