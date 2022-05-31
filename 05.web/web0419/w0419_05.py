from email import header
import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/index"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

# text를 lxml css파싱, beautifulSoup에서 html파싱해서 soup 가져옴
soup = BeautifulSoup(res.text,'lxml') 
# print(soup)
print('title : ', soup.title) 
print('title 제목 : ', soup.title.get_text())
print('a : ', soup.a)
print('a attr href: ',soup.a['href'] )
print('a text : ', soup.a.get_text()) # a: 원하는 태그 ==> text만 따로 얻을 수 있음
# print('div : ', soup.div)
# print('div : ', soup.div.attrs) # 속성
# print('div id : ',soup.div['id']) # 해당속성에 대한 value값을 나타냄
print('------------------')

print('div id = menu : ',soup.find('div',attrs={'id':'menu'})) # {속성값:value값}










# with open('bbb.html','w',encoding='utf-8') as f:
#     f.write(soup) # soup형태로 저장하게 되면 저장이 되지않음, 'w'로 지정되어 있지만 soup은 문자가 아니기때문에 저장할 수 없음