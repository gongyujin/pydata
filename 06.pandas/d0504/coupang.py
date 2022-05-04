# 1. 쿠팡
# 2. 
# 1) 카테고리별 추천 광고상품
# 가전디지털
# 바로가기>
# 2) 여성패션
# 바로가기>
# 주소찾기

# 3. 상품리스트 1개 출력
# 1)가전디지털 상품1개 출력
# 2)여성패션 상품 1개 출력


from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
browser=webdriver.Chrome(options=options)
options.add_experimental_option('detach',True)
browser.maximize_window()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })



# url='https://www.coupang.com/'
# browser.get(url)
# time.sleep(2)


# prev_height=browser.execute_script("return document.body.scrollHeight")
# while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(5)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if prev_height == curr_height:
#         break # 스크롤 크기가 더 이상 변경이 없을시 종료
#     prev_height = curr_height

   
# soup=BeautifulSoup(browser.page_source,'lxml')
# articles=soup.find('div',{'id':'categoryBestUnit'}).find_all('div',{'class':'category-best-unit'})

# for i,article in enumerate(articles):

#     print(article)
#     break


url='https://www.coupang.com/np/categories/178255?traid=home_CategoryBest_quick_link'
browser.get(url)
time.sleep(2)


prev_height=browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height

   
soup=BeautifulSoup(browser.page_source,'lxml')
articles=soup.find('ul',{'id':'productList'}).find_all('li')
for i,article in enumerate(articles):

    print(article)
    if i>=5:
        break
