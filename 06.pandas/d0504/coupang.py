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
options.headless=True
options.add_argument('window-size=1920x1080')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36')
browser=webdriver.Chrome(options=options)


options.add_experimental_option('detach',True)

url='https://www.coupang.com/'
browser.get(url)
time.sleep(2)


prev_height=browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height

time.sleep(10)    
soup=BeautifulSoup(browser.page_source,'lxml')
articles=soup.find('div',{'id':'container'}).find('section',{'id':'contents'})
print(articles)