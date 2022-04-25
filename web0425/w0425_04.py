# 네이버 페이지
# 지마켓을 검색해서 지마켓 페이지로 이동

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get('http://www.naver.com')

elem=browser.find_element_by_id('query')
elem.send_keys('지마켓')
elem.send_keys(Keys.ENTER)

elem=browser.find_element_by_link_text('쇼핑을 바꾸는 쇼핑')
elem.click()

# 다음페이지
# 부동산 검색

browser=webdriver.Chrome()
browser.get('https://www.daum.net/')

browser.find_element_by_id('q').send_keys('부동산')
browser.find_element_by_id('q').send_keys(Keys.ENTER)
elem=browser.find_element_by_id('q')
elem.send_keys('부동산')
elem.send_keys(Keys.ENTER)