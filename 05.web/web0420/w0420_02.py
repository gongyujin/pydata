import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

url='https://comic.naver.com/webtoon/list?titleId=703846&weekday=tue'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')

cartoons=soup.find_all('td',{'class':'title'})
for cartoon in cartoons:
    print('제목 : ', cartoon.a.get_text())
    car_href='https://comic.naver.com'+cartoon.a['href']
    print('바로가기 링크 : ', car_href)
    print("-"*20)