import requests
from bs4 import BeautifulSoup
import soupsieve

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

url="https://news.daum.net/"
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

# aurl=soup.find('div',{'class':'rc_info'}).a
# atxt=soup.find('div',{'class':'rc_info'}).a.get_text()
# print("https://comic.naver.com"+aurl['href'])
# print("실시간 인기 웹툰 : ",atxt)

# atag=soup.find('a',{'id':'recommand_titleName_0'})
# ahref=atag['href']
# print('1위 : ', atag.get_text())
# print("바로가기 링크 : ","https://comic.naver.com"+ahref)

atag=soup.find('a',{'class':'link_txt'})
ahref=atag['href']
print("최신뉴스1 : ",atag.get_text().strip())
print("바로가기 링크 : ",ahref)

