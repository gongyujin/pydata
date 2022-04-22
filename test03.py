# 년도별 통계를 화면에 출력하고, csv파일로 저장하시오.
import requests
from bs4 import BeautifulSoup
import csv

url='http://taas.koroad.or.kr/sta/acs/gus/selectTrnsportCnd.do?menuId=WEB_KMP_OVT_MVT_TAC_TAT'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

filename='연도별 교통요건.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)

title='년도	2016년	2017년	2018년	2019년	2020년'
title=title.split('\t')
writer.writerow(title)

rows=soup.find('table',{'class':'table01'}).tbody.find_all('tr')
for row in rows:
    columns=row.find_all('td')
    
    if len(columns)<1:
        continue
    
    data=[]
    for column in columns:
        data.append(column.get_text().strip())
    writer.writerow(data)
f.close()

rows2=soup.find('table',{'class':'table01'}).find_all('tr')
for row2 in rows2:
    
    rths=row2.find_all('th')
    rtds=row2.find_all('td')
    if rths:
        for rth in rths:
            print(rth.get_text().strip(),end='\t\t')
        print()
        print('-'*100)
    
    if rtds:
        for rtd in rtds:
            print(rtd.get_text().strip(),end='\t')
        print()
    
    