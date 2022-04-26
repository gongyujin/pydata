import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # 대기시간 사용을 위한 import
import random # 랜덤으로 input에 데이터 입력

# webdriver옵션 가져오기
options=webdriver.ChromeOptions()
# 브라우저 종료하지 않게 하는 options
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)


# 1. 크롬브라우저 생성
# browser=webdriver.Chrome()
# 2. 페이지 이동
browser.get('https://www.naver.com')

# 3. link_login 클래스 클릭해서 다시 페이지 이동
browser.find_element_by_class_name('link_login').click()

# 4. 대기시간을 적용, 랜덤으로 1초~3초사이 시간을 대기함.
time.sleep(random.uniform(1,3))

# 5. 자바스크립트 소스추가 및 자바스크립트 페이지 적용
input_js='document.getElementById("id").value="{id}";\
    document.getElementById("pw").value="{pw}"\
    '.format(id='admin',pw='1111')


# 자바스크립트 적용, input데이터 삽입
browser.execute_script(input_js)

# 6. 대기시간 적용
time.sleep(2)

# 7. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

# 메일 버튼 클릭
browser.find_element_by_link_text('메일').click()

time.sleep(2)
browser.find_element_by_xpath('//*[@id="smartFolderLayer"]/div/div/button').click()
time.sleep(2)

browser.find_element_by_link_text('메일쓰기').click()
time.sleep(2)

browser.find_element_by_id('toInput').send_keys('gyuj0114@naver.com')

time.sleep(2)

browser.find_element_by_id('subject').send_keys('테스트')
time.sleep(2)
browser.find_element_by_id('sendBtn').click()

time.sleep(20)


# selenium 방식으로 input 데이터 입력
# # id의 input선택
# elem=browser.find_element_by_name('id')
# # input aa입력
# elem.send_keys('aaa')
# # pw input 선택
# elem=browser.find_element_by_name('pw')
# # input 1111입력
# elem.send_keys('1111')
# # enter키 입력
# elem.send_keys(Keys.ENTER)