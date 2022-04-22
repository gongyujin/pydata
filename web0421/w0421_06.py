from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import csv # csv파일 라이브러리
import re

url='https://www.melon.com/chart/index.htm'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

filename='멜론 차트 순위.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)

title='순위 곡정보  앨범    좋아요'
title=title.split('\t')
writer.writerow(title)

data_rows=soup.find('table').tbody.find_all('tr')

for row in data_rows:
    columns=row.find_all('td')
    print(columns)
    if len(columns) <=1:
        continue
    data=[]
    for column in columns:
        rank=column.find('span',{'class':'rank'})
        title=column.find('div',{'class':'wrap_song_info'})
        print(rank)
        print(title)
        break
    # data.append(column.get_text().strip())
    # writer.writerow(data)
    
f.close()
            
        # if column.div['class']!='wrap t_center':
        #     print(column)
            