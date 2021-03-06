import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv 
import time # 대기시간 사용을 위한 import
import random # 랜덤으로 input에 데이터 입력

# 출력화면이 나타날때까지 대기하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 라이브러리
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)

# 브라우저에서 url사이트를 실행
url="https://flight.naver.com/"
# 윈도우 창 최대화
browser.maximize_window()
browser.get(url)
time.sleep(2)

# 항공권 출발선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/b').click()
time.sleep(2)
# 국내부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]\
    /div[2]/section/section/button[1]').click()
time.sleep(2)
# 서울부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]\
    /div[2]/section/section/div/button[1]').click()
time.sleep(2)

# 항공권 도착선택
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
# elements_by_class_name : 모든 class다 가져옴
browser.find_elements_by_class_name('select_code__d6PLz')[1].click() # 0번째는 출발부분을 선택하는 것
time.sleep(2)
# 국내부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]\
    /div[2]/section/section/button[1]').click()
time.sleep(2)
# 제주부분 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]\
    /div[2]/section/section/div/button[2]').click()
time.sleep(2)
# 가는날/오는날 선택
# 가는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
# 24일 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[3]/button').click()
time.sleep(2)
# 오는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(2)
# 25일 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button').click()
time.sleep(2)

# 인원수 선택
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()

# 항공권 검색버튼 클릭
browser.find_element_by_class_name("searchBox_txt__3RoCw").click()


# 페이지 로딩완료까지 대기
# 브라우저 로딩후 10초대기, 화면에서 선택한 요소(xpath)가 있는지 체크
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]')))
# time.sleep(10)

# 현재 높이 가져옴.
prev_height = browser.execute_script("return document.body.scrollHeight")



# 무한반복
while True:
    # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 열리는 동안 대기
    time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    # 무한반복 끝



# 현재 웹페이지 html소스를 가져옴.
page_html = browser.page_source
# BeautifulSoup html파싱
soup = BeautifulSoup(page_html,"lxml")


# csv 파일 저장
filename='airline.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')

writer=csv.writer(f)

title='항공사 이름,가격,출발시간,도착시간'
title=title.split(',')
writer.writerow(title)

flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA result"})
choice=[]
for flight in flights:
    price=flight.find('div',{'class':'domestic_prices__3N88F'}).find('b',{'class':'domestic_price__1qAgw'}).i.get_text()
    name=flight.find('div',{'class':'domestic_item__2B--k'}).find('div',{'class':'airline'}).b.get_text()
    price=price.replace(',','')
    price=int(price)
    stime=flight.find('div',{'class':'domestic_item__2B--k'}).find('div',{'class':'route_Route__2UInh'}).find('span',{'class':'route_airport__3VT7M'}).b.get_text()
    ftime=flight.find('div',{'class':'domestic_item__2B--k'}).find('div',{'class':'route_Route__2UInh'}).find('span',{'class':'route_airport__3VT7M'}).next_sibling.b.get_text()
    data=[]
    if price <= 50000:
        choice.append(price)
        data.append(name)
        data.append(price)
        data.append(stime)
        data.append(ftime)
        print('항공사 이름: {}'.format(name))
        print('가격 : {}원'.format(price))
        print('출발시간 : {}'.format(stime))
        print('도착시간 : {}'.format(ftime))
        print('-'*30)
        writer.writerow(data)
print()
        
print("5만원 이하 검색 개수 : ",len(choice))

f.close()
