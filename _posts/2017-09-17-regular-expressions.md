# 	정규표현식 (Regular Expressions)
###### 복잡한 문자열을 처리할 때: 파이썬에서는 표준 모듈 `re` 를 사용.

```
import re
result = re.match('dog', 'dog, Canis lupus familiaris')
print(result.group())
```
복잡하거나 자주 사용될 땐 **컴파일**을 이용하자.

1. match: 패턴과 문자열을 비교해서 일치하면 Match object를 반환.
	- 시작부터 일치하는 패턴을 찾기 때문에 중간에 나오는 패턴은 다르게 처리.

	```
	source = 'dog, Canis lupus familiaris'
	m = re.match('.*lupus', source)
	if m:
	...print(m.group())
	...
	dog, Canis lupus
	```
	* `.`: 문자열 1개.
	* `*`: 해당 패턴이 0개 이상 올 수 있음.
2. search: 첫번째 일치하는 패턴.
	```
	m = re.search('.*lupus', source)
	if m:
	...print(m.group())
	...
	>>>lupus
	```
3. findall: 일치하는 모든 패턴.
	```
	m = re.findall('u..', source)
	m
	>>>['upu']
	```
	끝자리에 오는 글자를 찾으려면
	```
	m = re.findall('s.?.?', source)
	m
	>>>['s l', 's f', 's']
	```
4. split: 패턴으로 나누기.
	```
	m = re.split('s', source)
	m
	>>>['Cani', ' lupu', ' familiari', '']
	```
5. sub: 패턴 대체.
	```
	m = re.sub('s', '!', source)
	>>>'Cani! lupu! familiari!'
	```
6. 정규표현식의 패턴문자
	패턴 | 문자
	----|----
	\d  | 숫자
	\D  | 비숫자
	\w  | 문자
	\W  | 비문자