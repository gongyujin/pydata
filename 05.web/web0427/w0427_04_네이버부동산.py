from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyautogui

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

browser=webdriver.Chrome(options=options)

url='https://new.land.naver.com/complexes/2992?ms=37.543599,126.95604,17&a=APT:ABYG:JGC&e=RETAIL'
browser.maximize_window()
browser.get(url)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="complexOverviewList"]/div[2]/div[1]/div[2]/div/div[1]/button').click()
browser.find_element_by_xpath('//*[@id="complexOverviewList"]/div[2]/div[1]/div[2]/div/div[1]/div/div/ul/li[2]/label').click()
browser.find_element_by_xpath('//*[@id="complexOverviewList"]/div[2]/div[1]/div[2]/div/div[1]/button').click()
time.sleep(2)

prev_height= browser.execute_script("return articleListArea.scrollHeight")

while True:
    pyautogui.moveTo(250,750) 
    pyautogui.scroll(-prev_height)
    time.sleep(2)

    curr_height=browser.execute_script("return articleListArea.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height=curr_height
    
    
time.sleep(2)
soup=BeautifulSoup(browser.page_source,'lxml')
house_list=soup.find('div',{'class':'item_area'}).find('div',{'id':'articleListArea'})
houses=house_list.find_all('div',{'class':'item false'})
house=houses[49]

title=house.find('span',{'class':'text'}).get_text()
price_type=house.find('span',{'class':'type'}).get_text()
price=house.find('span',{'class':'price'}).get_text()
info_type=house.find('div',{'class':'info_area'}).p.strong.get_text()
info_spec=house.find('div',{'class':'info_area'}).find('span',{'class':'spec'}).get_text()
info=house.find('div',{'class':'info_area'}).p.find_next_sibling('p').get_text()

print('이름 : ',title)
print('거래방식 : ',price_type)
print('금액 : ',price)
print('매물정보 : ',info_type)
print('면적, 층수, 방향 : ',info_spec)
print('매물특징 : ',info)

