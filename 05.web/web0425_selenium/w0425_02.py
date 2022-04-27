import requests
# from bs4 import BeautifulSoup
from selenium import webdriver # 웹브라우저를 열겠다는 의미
# selenium의 key동작 라이브러리 : 키보드에 있는 것을 할당받겠다는 의미
from selenium.webdriver.common.keys import Keys 

# webdriver 크롬브라우저 변수 할당
browser=webdriver.Chrome()
# 브라우저에서 url사이트를 실행
browser.get('http://www.naver.com')
# class name link_login 선택
elem=browser.find_element_by_class_name('link_login')
print(elem)
# elem을 클릭
elem.click()

elem=browser.find_element_by_id('id')
# elem에 aaa 글자 입력
elem.send_keys('aaa')
# elem=browser.find_element_by_id('pw')
# xpath로 선택
elem=browser.find_element_by_xpath('//*[@id="pw"]')
# elem에 1111 글자 입력
elem.send_keys('1111')

elem=browser.find_element_by_id('log.login')
# elem enter키 입력
elem.send_keys(Keys.ENTER)
# 페이지 뒤로 가기
browser.back()
# 페이지 앞으로 가기
browser.forward()
# 페이지 새로고침 (f5)
browser.refresh()


# url ="http://www.naver.com"
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

# res=requests.get(url,headers=headers)
# res.raise_for_status()
# soup=BeautifulSoup(res.text,'lxml')
# soup.find('div',{'id':'aaa'}) # selenium에서는 안됨

