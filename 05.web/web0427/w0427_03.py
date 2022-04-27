# [ 뉴스 ]
# 네이버>증권>주요뉴스 6개
# 제목, 링크주소 6개 

# [ 주식정보 ]
# 금융검색 : 삼성전자
# 삼성전자(종목명, 현재가, 전일대비, 등락율, 매도호가, 매수호가, 거래량, 거래대금)

# [ 날씨 ]
# 네이버 날씨, 주간예보의 오늘오전,오늘오후,내일 날씨
# ex) 오늘오전 맑음 10/21 내일 맑음 흐림 11/22

# 파일첨부
# 멜론 1-100위까지 csv파일로 저장
# ex) 순위, 곡정보 (제목,가수), 앨범,좋아요

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import csv

filename='멜론 1-100위.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)

title='순위,제목,가수,앨범명,좋아요 수'.split(',')
writer.writerow(title)

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

browser=webdriver.Chrome(options=options)

url='https://www.naver.com/'
browser.get(url)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[3]/a').click()

time.sleep(2)
soup=BeautifulSoup(browser.page_source,'lxml')

texts=soup.find('div',{'class':'section_strategy'})
text=texts.find_all('li')

content=''
content+='[ 뉴스 ]\n'
for txt in text:
    title=txt.find('a').get_text()
    link="https://www.naver.com"+txt.find('a')['href']
    content+=title
    content+='\n'
    content+=link
    content+='\n'
content+='\n'

browser.find_element_by_id('stock_items').send_keys('삼성전자')
browser.find_element_by_id('stock_items').send_keys(Keys.ENTER)

time.sleep(2)
soup=BeautifulSoup(browser.page_source,'lxml')
table=soup.find('table',{'class':'tbl_search'})
ths=table.find('thead').find_all('th')
tds=table.find('tbody').find('tr').find_all('td')

content+='[ 주식정보 ]\n'
for i in range(len(ths)):
    title=ths[i].get_text().strip()
    con=tds[i].get_text().strip()
    
    line=title+' : '+con
    content+=line
    content+='\n'
content+='\n' 
    
    
url='https://weather.naver.com/'
browser.get(url)
time.sleep(2)
soup=BeautifulSoup(browser.page_source,'lxml')

section=soup.find('div',{'id':'weekly'})
todaywe=section.find('ul',{'class':'box_color'}).find('li',{'class':'item'})

am=todaywe.span.span.strong.get_text()
todayinf_am=todaywe.find('i',{'class':'ico _cnLazy ico_wt1'}).get_text()
todaytemp_am=todaywe.find('span',{'class':'data lowest'}).get_text()
todaytemp_am=re.sub(r'[^0-9]','',todaytemp_am)

pm=todaywe.find_next_sibling('li').span.span.strong.get_text()
todayinf_pm=todaywe.find_next_sibling('li').find('i',{'class':'ico _cnLazy ico_wt1'}).get_text()
todaytemp_pm=todaywe.find_next_sibling('li').find('span',{'class':'data highest'}).get_text()
todaytemp_pm=re.sub(r'[^0-9]','',todaytemp_pm)

tomorrow=section.find('div',{'class':'scroll_area'}).find('li',{'class':'week_item'}).find_next_sibling('li')
tomorrowwe=tomorrow.find('span',{'class':'date_inner'}).strong.get_text()
tomorrowinf_am=tomorrow.find('div',{'class':'cell_weather'}).find('i',{'class':'ico _cnLazy ico_wt1'}).span.get_text()
tomorrowinf_pm=tomorrow.find('div',{'class':'cell_weather'}).find('span',{'class':'weather_inner'}).find_next_sibling('span').i.span.get_text()
tomorrowtemp_am=tomorrow.find('div',{'class':'cell_temperature'}).find('span',{'class':'lowest'}).get_text()
tomorrowtemp_pm=tomorrow.find('div',{'class':'cell_temperature'}).find('span',{'class':'highest'}).get_text()
tomorrowtemp_am=re.sub(r'[^0-9]','',tomorrowtemp_am)
tomorrowtemp_pm=re.sub(r'[^0-9]','',tomorrowtemp_pm)

content+='[ 날씨 ]\n'
content=content+am+'\t'
content=content+todayinf_am+'\t'
content=content+todaytemp_am+'\n'
content=content+pm+'\t'
content=content+todayinf_pm+'\t'
content=content+todaytemp_pm+'\n'

content=content+tomorrowwe+'\t'
content=content+tomorrowinf_am+'/'
content=content+tomorrowinf_pm+'\t'
content=content+tomorrowtemp_am+'/'
content=content+tomorrowtemp_pm+'\n'

print(content)

url='https://www.melon.com/chart/index.htm'
browser.get(url)
time.sleep(3)
soup=BeautifulSoup(browser.page_source,'lxml')
song_infs=soup.find('div',{'id':'tb_list'}).table.tbody.find_all('tr')

for song_inf in song_infs:
    columns=song_inf.find_all('td')
    data=[]
    for i,column in enumerate(columns):
        if i==1:
            rank=column.get_text().strip()
        elif i==5:
            name=column.find('div',{'class':'ellipsis rank01'}).get_text().strip()
            singer=column.find('div',{'class':'ellipsis rank02'}).a.get_text().strip()
        elif i==6:
            album=column.get_text().strip()
        elif i==7:
            like=column.find('span',{'class':'cnt'}).get_text().strip()
            like=re.sub(r'[^0-9,]','',like)

    data.append(rank)
    data.append(name)
    data.append(singer)
    data.append(album)
    data.append(like)
    writer.writerow(data)
        
f.close()
browser.quit()

smtpName='smtp.naver.com'
smtpPort=587
sendEmail="gyuj014@naver.com"
password="1111"
recvEmail="onulee@naver.com"

msg=MIMEMultipart('alternative')
part2=MIMEText(content)

msg.attach(part2)
msg['From']=sendEmail
msg['To']=recvEmail
msg['Subject']='파이썬 수업_뉴스,주식정보,날씨,멜론차트'

part=MIMEBase('application','octet-stream')

with open('멜론 1-100위.csv','rb') as f:
    part.set_payload(f.read())
    
encoders.encode_base64(part)

part.add_header('Content-Disposition','attachment',filename='멜론 1-100위.csv')

msg.attach(part)

s=smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,password)
s.sendmail(sendEmail,recvEmail,msg.as_string())

print('메일발송이 완료되었습니다.')
s.close()

# # MIME 객체생성
# msg = MIMEMultipart("mixed")
# # 첨부파일 경로/이름 지정하기
# filename='시가총액1-200.csv'  
# part = MIMEBase('application','octet-stream')
# attachment =open(filename,'rb')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition',"attachment", filename= os.path.basename(filename))
# msg.attach(part)