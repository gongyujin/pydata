# 날짜, 금액, text, 폰모델/ 출고가, 제조사/ 이동통신물가지수 => 2000개
# 폰가격 예측
#크롬 웹드라이버 관리 라이브러리 호출

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv 
import time # 대기시간 사용을 위한 import
import random # 랜덤으로 input에 데이터 입력
import pyautogui

# 출력화면이 나타날때까지 대기하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 라이브러리
from selenium.webdriver.support import expected_conditions as EC



# webdriver 크롬브라우저 변수 할당 
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
browser = webdriver.Chrome(options=options)


url='https://web.joongna.com/search/category?category=1150'

browser.get(url)


# #스크롤내림
prev_height = browser.execute_script("return document.body.scrollHeight")
# 무한반복
count = 0
while True:
    count += 1
    # 12 개씩. 10 번
    # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # scroll(+) 위쪽으로 스크롤  scroll(-) 아래쪽으로 스크롤
    pyautogui.moveTo(500,500)
    pyautogui.scroll(-prev_height)
    # 모니터 해상도의 절대 값을 사용하여 옮길 수 있다. 
    # pyautogui.moveTo(200,200)
    
    # 페이지 열리는 동안 대기
    time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if count == 100:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    


time.sleep(random.uniform(1,3))
# 현재 웹페이지 html소스를 가져옴.
page_html = browser.page_source
# BeautifulSoup html파싱
soup = BeautifulSoup(page_html,"lxml")


# csv 파일 저장
filename='phone info_중고나라.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')

writer=csv.writer(f)

title='폰모델 제목,가격,등록시간,내용'
title=title.split(',')
writer.writerow(title)


divs=soup.find_all('div',{'class':'ant-col col css-t7ixlq e312bqk0'})

for div in divs:
    data=[]
    main_url='https://web.joongna.com'
    url=main_url+div.find('a')['href']
    browser.get(url)
    page_html = browser.page_source
    # BeautifulSoup html파싱
    soup = BeautifulSoup(page_html,"lxml")
    title=soup.find('h1').get_text()
    price=soup.find('p',{'class':'css-1artofo'}).get_text().split('원')[0]
    price=price.replace(',','')
    price=int(price)
    time = '2022-07-08'
    context=soup.find('p',{'class':'content'}).get_text()
 
    data.append(title)
    data.append(price)
    data.append(time)
    data.append(context)
    writer.writerow(data)

f.close()
    
    
