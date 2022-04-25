import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# webdriver옵션 가져오기
options=webdriver.ChromeOptions()
# 브라우저 종료하지 않게 하는 options
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)
# res=requests.get('https://finance.naver.com/') # 정보가 제대로 들어오지않을때는 selenium으로 가져와야함

# browser=webdriver.Chrome()
browser.get("http://www.melon.com/chart/index.htm")
page_url=browser.page_source
soup=BeautifulSoup(page_url,'lxml')

# selenium으로 html소스 가져오기
charts=soup.find_all('tr',{'class':'lst50'})
print(charts[0].find('div',{'class':'ellipsis rank03'}).get_text())
print(charts[0].find('span',{'class':'cnt'}))
# cnt에 숫자는 전체페이지가 돌고 그다음에 들어오기때문에 requests로는 읽을 수 없음




# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
# url="http://www.melon.com/chart/index.htm"
# res=requests.get(url,headers=headers)
# soup=BeautifulSoup(res.text,'lxml')

# # 멜론 좋아요 숫자 출력, 숫자 js로 되어있기에 requests로는 출력이 안됨
# charts=soup.find_all('tr',{'class':'lst50'})
# print(charts[0].find('div',{'class':'ellipsis rank03'}).get_text())
# print(charts[0].find('span',{'class':'cnt'}))

# browser=webdriver.Chrome()
# browser.get('https://www.naver.com')


# browser.find_element_by_link_text('증권').click()

# # 현재페이지 url 가져오기
# page_url=browser.page_source

# # res=requests.get('http://www.naver.com')
# # url 소스 html 파싱
# soup=BeautifulSoup(page_url,'lxml')
# # html소스 출력
# with open('elum.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
    
# # print(soup.prettify())