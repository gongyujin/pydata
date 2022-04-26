import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# options.headless=True
# options.add_argument('window-size=1920x1080')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36')

browser=webdriver.Chrome(options=options)

url="https://www.google.com/"
browser.get(url)
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('한소희')

browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
time.sleep(2)


browser.find_element_by_xpath('//*[@id="rso"]/div[6]/div/div[1]/div/div/div[1]/div[1]/div/a/h3').click()
time.sleep(2)

prev_height=browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    
    curr_height=browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        break
    prev_height=curr_height
    
soup=BeautifulSoup(browser.page_source,'lxml')

title=soup.find('h1',{'class':'headline'}).get_text()
txts=soup.find('div',{'class':'article_body fs3'})
txt_1=txts.find_all('p')

re_text=''
for txt in txt_1:
    re_text+=txt.get_text()
    

smtpName="smtp.naver.com" # 메일서버주소
smtpPort=587 # 메일서버 포트번호


sendEmail="gyuj0114@naver.com" # 자신의 아이디
password="alfk47430990" # 자신의 비밀번호
recvEmail="mayitshe87@naver.com" # 받는사람 주소


# 글쓰기 제목, 내용
content=re_text

# MIME 객체
msg=MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['Subject']=title


# 메일서버주소 정보 예시) smtp.naver.com/587
s=smtplib.SMTP(smtpName,smtpPort)
# 메일서버접근
s.starttls()
# 메일서버로그인
s.login(sendEmail,password)
# 메일발송
s.sendmail(sendEmail,recvEmail,msg.as_string())
# 메일 닫기
s.close()