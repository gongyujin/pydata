import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import pyautogui
import csv

# csv 파일 저장
filename='google_movie.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='') 
writer=csv.writer(f)
# 상단제목
title='제목,평점,가격,링크'.split(',')
writer.writerow(title)


# webdriver옵션 가져오기
options=webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option('detach',True)
# 화면 열리지 않고 실행
options.headless=True
# 화면 최대화
options.add_argument('window-size=1920x1080')

# 브라우저 열기
browser=webdriver.Chrome(options=options)

url="https://play.google.com/store/movies/category/MOVIE"
# 사이트열기
browser.get(url)
time.sleep(2)

# 자바스크립트 실행
prev_height= browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # scroll(+)로 정의하면 위쪽으로 이동, scroll(-)로 정의하면 아래쪽으로 이동
    # pyautogui.moveTo(500,500) # 마우스 중앙으로 이동 # 해상도에 맞는 절대적위치를 의미함
    # pyautogui.scroll(-prev_height) # 마우스 아래로 이동 # 마우스의 움직임을 나타내는것 ==> scrollHeight랑 같은 의미로 사용됨
    time.sleep(2)

    curr_height=browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height=curr_height
    
# 화면캡쳐
browser.get_screenshot_as_file('googleMovie_screenshot.jpg')

time.sleep(2) 
soup=BeautifulSoup(browser.page_source,'lxml')

# zuJxTd 클래스 검색시 9개 검색이 됨. 마지막 9번째가 찾으려고 하는 것임
movies=soup.find_all("div",{"class":"zuJxTd"})
# 리스트[8]: 가족과 함께 보는 영화 콜렉션 가져옴
movies=movies[8]
movie_lists=movies.find_all('div',{'class':'ULeU3b neq64b'}) # 20개 영화를 가져옴


for movie in movie_lists:
    data=[]
    title=movie.find('div',{'class':'Epkrse'}).get_text()
    # 평점
    rate=movie.find('div',{'class':'LrNMN'}).get_text()
    # 0-9까지 숫자와 .을 제외한 것은 모두 삭제처리
    rate=float(re.sub(r'[^0-9.]','',rate))
    # 가격
    price=movie.find('div',{'class':'LrNMN'}).next_sibling.span.span.get_text()
    price=int(re.sub(r'[^0-9]','',price))
    # 링크
    link=movie.find('a',{'class':'Si6A0c ZD8Cqc'})['href']
    link='https://play.google.com'+link
    # 이미지
    img=movie.find('div',{'class':'TjRVLb'}).img['src']
    if img.startswith('//'):
        img="https:"+img
        
    # 금액대가 6천원이하인것만 출력 아니면 스킵
    if price > 6000:
        continue

    data.append(title)
    data.append(rate)
    data.append(price)
    data.append(link)
    writer.writerow(data)
    
    
    # 화면출력
    print("영화제목 : ",title)
    print("별점 : ",rate)
    print("가격 : ",price)
    print("링크 : ",link)
    print("이미지 링크 : ",img)
    print('-'*50)

    # 이미지 다운로드
    img_res=requests.get(img)
    img_res.raise_for_status()
    with open("movie_img_{}.jpg".format(title),'wb') as f:
        f.write(img_res.content)

f.close()

# browser.close() # 탭 1개만 닫음
# time.sleep(4)
browser.quit() # 브라우저 모두 종료

# 최종정리
# 1. 구글무비-한국어지정
# 2. 가기고 올 위치 지정:section list[8
# 3. 평점 -> 숫자와 점만 분리해서 float 형변환
# 4. 가격 -> 숫자만 분리해서 int형변환
# 5. 가격비교
# 6. csv파일 저장방법
# 7. 이미지 다운로드 저장방법


# 국문페이지 설정 ==> 현재가지고와야하는 language가 무엇인지 설정해줘야함
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",\
#     "Accept-Language":"ko-KR,ko"}
# res=requests.get(url,headers=headers)
# res.raise_for_status()

# soup=BeautifulSoup(res.text,'lxml')

# print(soup.prettify())

# with open("movie.html",'w',encoding="utf-8") as f:
#     f.write(soup.prettify())