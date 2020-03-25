import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    a_tag = song.select_one('td.info > a')
    if a_tag is not None:
        title = a_tag.text
        title = title.replace("                                    ", "")
        title = title.split('\n')
        rank = song.select_one('.number').text
        rank = rank.replace(" ", "")
        rank = rank.split('\n')
        singer = song.select_one('.artist').text
        print(rank[0], title[-1], singer)
