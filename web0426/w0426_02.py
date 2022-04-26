# 1. 야놀자 페이지
# 2. 검색창: 제주리조트 검색어를 삽입
# 3. 날짜 5/27-28
# 4. 검색페이지 이동 후 스크롤 내림
# 5. 출력(제목,평점,금액,링크) : 평점 4.0이상
# 6. csv파일저장, 사진저장

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import pyautogui
import csv

# 출력화면이 나타날때까지 대기하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 라이브러리
from selenium.webdriver.support import expected_conditions as EC

filename='yanolja.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)

# ,로 분리해서 list타입으로 반환
title='숙소명,평점,금액,링크'.split(',')
# title csv에 저장
writer.writerow(title)

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)

url="https://www.yanolja.com/"
browser.get(url)
time.sleep(2)

browser.find_element_by_class_name('HomeSearchBar_search__3R15k').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[2]/button[1]').click()
time.sleep(2)

browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[6]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[7]').click()
time.sleep(2)

browser.find_element_by_class_name('DateRangePicker_rangePickerConfirmButton__2c41H').click()
time.sleep(2)
browser.find_element_by_class_name('SearchInput_input__342U2').send_keys('제주리조트')

time.sleep(2)

browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[1]/div/button[2]/img').click()

WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[1]/main/div/section[2]/div/div/div[1]')))

prev_height=browser.execute_script('return document.body.scrollHeight')

while True:
    pyautogui.scroll(-prev_height)
    time.sleep(2)
    
    curr_height=browser.execute_script('return document.body.scrollHeight')
    if prev_height==curr_height:
        break
    prev_height=curr_height

# # 화면 스크린샷
# browser.get_screenshot_as_file('yanolja.jpg')
    
time.sleep(2)

soup=BeautifulSoup(browser.page_source,'lxml')
trips=soup.find_all('div',{'class':'PlaceListItemText_container__fUIgA text-unit'})
count=0
for trip in trips:
    
    # 제목
    title=trip.find('div',{'class':'PlaceListTitle_container__qe7XH'}).strong.get_text()
    # 별점
    rate=trip.find('span',{'class':'PlaceListScore_rating__3Glxf'})
    # 금액
    price=trip.find('span',{'class':'PlacePriceInfo_salePrice__28VZD'}).get_text()
    # price=re.sub(r'[^0-9]','',price)
    # 링크
    link=trip.a['href']
    if link.startswith('/'):
        link='https://www.yanolja.com'+link
    # 이미지
    img=trip.find('div',{'class':'PlaceListImage_imageText__2XEMn'})['style']
    temp=img.find('https')
    img=img[temp:-3]
      
    if rate:
        rate=float(rate.get_text())
        if rate < 4.0:
            continue
    else:
        # 평점이 없을 시 제외
        continue 
    
    count+=1  
    print('숙소명 : ',title)
    print('별점 : ',rate)
    print('금액 : ',price)
    print('링크 : ',link)
    print('-'*50)
    
    # csv에 숙소정보 저장
    data=[]
    data.append(title)
    data.append(rate)
    data.append(price)
    data.append(link)
    writer.writerow(data)
    
    # 이미지 다운로드
    img_res=requests.get(img)
    img_res.raise_for_status()
    with open('trip_{}.jpg'.format(count),'wb') as f:
        f.write(img_res.content)
        
f.close()
browser.quit()