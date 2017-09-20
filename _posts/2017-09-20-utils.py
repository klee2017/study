import requests

from collections import namedtuple
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

Episode = namedtuple('Episode', ['no', 'img_url', 'title', 'rating', 'created_date'])
# 클래스를 대신해주는 리스트를 갖는 튜플.
# 순서를 지켜서 클래스처럼 사용.
# 저장해야할 정보들.

# url에서 물음표 앞은 주소 뒤는 key와 value로 이루어진 parameter.
# key와 value들은 &기호로 줄줄이 나옴.

def get_webtoon_episode_list(webtoon_id, page=1):
"""
특정 페이지의 episode list를 return.
:param webtoon_id: 웹툰 고유 ID. 맨 위상단에 titleid로 써 있는것.
:param page: 가져오려는 Episode list 페이지.
우선 1페이지.
:return: list(Episode)
"""
    webtoon_list_url = 'http://comic.naver.com/webtoon/list.nhn'
    #먼저 고유주소.
    params = {
            'titleId':webtoon_id,
            'page':page,
            }
#파라미터를 정리.
    reponse = requests.get(webtoon_list_url, params=params)
#페이지에 리퀘스트를 요청해서 reponse를 받아옴.
    
