import requests
from bs4 import BeautifulSoup

webtoon_url = 'http://comic.naver.com/webtoon/list.nhn?titleId=697680&weekday=mon'

response = requests.get(webtoon_url)
source = response.text
soup = BeautifulSoup(source)
print(soup.prettify())

with open('born.txt', 'wt') as f:
    f.write(soup.prettify())
