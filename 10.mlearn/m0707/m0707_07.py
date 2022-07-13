# # 날짜, 금액, text, 폰모델/ 출고가, 제조사/ 이동통신물가지수 => 2000개
# # 폰가격 예측
# #크롬 웹드라이버 관리 라이브러리 호출

# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import csv 
# import time # 대기시간 사용을 위한 import
# import random # 랜덤으로 input에 데이터 입력

# # 출력화면이 나타날때까지 대기하는 라이브러리
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# # 브라우저 화면의 상태를 알려주는 라이브러리
# from selenium.webdriver.support import expected_conditions as EC
# browser=webdriver.Chrome()

# for i in range(21,31):
#     url='https://m.bunjang.co.kr/categories/600700001?page='+str(i)+'&order=date'
#     browser.get(url)
#     time.sleep(3)

#     # csv 파일 저장
#     filename='phone info3.csv'
#     f=open(filename,'w',encoding='utf-8-sig',newline='')

#     writer=csv.writer(f)

#     title='폰모델 제목,가격,등록시간,내용'
#     title=title.split(',')
#     writer.writerow(title)

#     # 현재 웹페이지 html소스를 가져옴.
#     page_html = browser.page_source
#     # BeautifulSoup html파싱
#     soup = BeautifulSoup(page_html,"lxml")
#     divs=soup.find_all('div',{'class':'sc-ejGVNB jrCaJ'})
#     print(len(divs))
#     for div in divs:
#         print(i)
#         data=[]
#         main_url='https://m.bunjang.co.kr'
#         url=main_url+div.find('a')['href']
#         print(url)
#         browser.get(url)
#         time.sleep(2)
#         page_html = browser.page_source
#         # BeautifulSoup html파싱
#         soup = BeautifulSoup(page_html,"lxml")
#         if soup.find('div',{'class':'sc-jrIrqw deihsD'}):
#             title=soup.find('div',{'class':'sc-jrIrqw deihsD'}).get_text()
#         else:
#             title=''
#         if soup.find('div',{'class':'sc-iQtOjA beRPoY'}):
#             price=soup.find('div',{'class':'sc-iQtOjA beRPoY'}).get_text().split('원')[0]
#         else:
#             price=''
#         if soup.find('div',{'class':'sc-fyjhYU dRDSys'}):
#             if soup.find('div',{'class':'sc-fyjhYU dRDSys'}).find('div',{'class':'sc-ugnQR bHzOsq'}):
#                 times=soup.find('div',{'class':'sc-fyjhYU dRDSys'}).find('div',{'class':'sc-ugnQR bHzOsq'}).find('div',{'class':'sc-eIHaNI kvuSXN'})
#                 time1=times.find_all('div',{'class':'sc-eTpRJs jbRTcu'})[2].get_text()
#             else:
#                 time1=''
#         else:
#             time1=''
#         if soup.find('div',{'class':'sc-eLdqWK evwfQs'}):
#             context=str(soup.find('div',{'class':'sc-eLdqWK evwfQs'}).get_text())
#         else:
#             context=''
        
#         data.append(title)
#         data.append(price)
#         data.append(time1)
#         data.append(context)
#         writer.writerow(data)

# f.close()
        
        
        
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv ,re
import time # 대기시간 사용을 위한 import
import random # 랜덤으로 input에 데이터 입력

# 출력화면이 나타날때까지 대기하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 라이브러리
from selenium.webdriver.support import expected_conditions as EC
browser= webdriver.Chrome()
filename='phone_info3.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')

writer=csv.writer(f)

title='폰모델 제목,가격,등록시간,내용'
title=title.split(',')
writer.writerow(title)
for i in range(21,31):
    url='https://m.bunjang.co.kr/categories/600700001?page='+str(i)+'&order=date'
    browser.get(url)
    time.sleep(5)
    # csv 파일

 
    # 현재 웹페이지 html소스를 가져옴.
    page_html = browser.page_source
    # BeautifulSoup html파싱
    soup = BeautifulSoup(page_html,"lxml")
    divs=soup.find_all('div',{'class':'sc-ejGVNB jrCaJ'})
    # print(len(divs))
    for i,div in enumerate(divs):
        print(i)
        data=[]
        main_url='https://m.bunjang.co.kr'
        url=main_url+div.find('a')['href']
        browser.get(url)
        time.sleep(3)
        page_html = browser.page_source
        # BeautifulSoup html파싱
        soup = BeautifulSoup(page_html,"lxml")
        times=soup.find('div',{'class':'sc-fyjhYU dRDSys'}).find('div',{'class':'sc-ugnQR bHzOsq'}).find('div',{'class':'sc-eIHaNI kvuSXN'})
        if not times:
            continue
        times=soup.find('div',{'class':'sc-fyjhYU dRDSys'}).find('div',{'class':'sc-ugnQR bHzOsq'}).find('div',{'class':'sc-eIHaNI kvuSXN'})
        title=soup.find('div',{'class':'sc-jrIrqw deihsD'}).get_text()
        price=soup.find('div',{'class':'sc-iQtOjA beRPoY'}).get_text()
        time1=times.find_all('div',{'class':'sc-eTpRJs jbRTcu'})[2].get_text()
        context=soup.find('div',{'class':'sc-eLdqWK evwfQs'}).get_text()    
        if price=='연락요망':
            data.append(price)
        else:    
            price=re.sub(r"원",'',price)
            price=int(re.sub(r',','',price))
        data.append(title)
        data.append(price)
        data.append(time1)
        data.append(context)
        writer.writerow(data)
        print('제목',title)
        print('가격',price)
        print('날짜',time1)
        print('내용',context)
f.close()
browser.quit()

# print(times)
# warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
# url="https://m.bunjang.co.kr/categories/600700001?page=1&order=date"

# browser.maximize_window()
# browser.get(url)

# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[3]/div/div[1]').click()


# browser.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]').click()
# 가격 제조사, 날짜 , 모델명, 내용
# page_html =browser.page_source



# soup = BeautifulSoup(url,'lxml')
# xx =soup.find("div",{"class":"sc-dEfkYy cUFeQg"})
# sc-dHmInP ldHdsu
# print(xx)
# filename="제주도저가.csv"
# f=open(filename,"w",encoding="utf-8 sig")
# writer = csv.writer(f)
# title=["제조사","날짜","가격","도착시간"]
# writer.writerow(title)
# for i, flight in enumerate(flights):
    
#     goair=[]
#     price=flight.find("i",{"class":"domestic_num__2roTW"}).get_text()
#     price=int(re.sub(r',','',price))
#     fname=flight.find("b",{"class":"name"}).get_text()
#     st=flight.find_all("b",{"class":"route_time__-2Z1T"})[0].get_text()
#     rt=flight.find_all("b",{"class":"route_time__-2Z1T"})[1].get_text()
#     if price <50000:
#         goair.append(fname)
#         goair.append(price)
#         goair.append(st)
#         goair.append(rt)
#         writer.writerow(goair)
# f.close()