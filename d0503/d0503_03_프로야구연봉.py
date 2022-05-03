# 2022년 연봉.csv
# 2021년 연봉.csv
# 2020년 연봉.csv
import requests
from bs4 import BeautifulSoup
import re
import csv

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

for year in range(2020,2023):
           
    filename=str(year)+'년연봉.csv'
    f=open(filename,'w',encoding='utf-8-sig',newline='')
    writer=csv.writer(f)

    title='선수이름,연도,팀,연봉(만원),WAR'
    title=title.split(',')
    writer.writerow(title)

    url='http://www.statiz.co.kr/salary.php?opt=0&sopt={}&te='.format(year)
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')

    table=soup.find('div',{'class':'col-xs-12 col-sm-6'})
    players=table.find_all('tr')

    for i,player in enumerate(players):
        if i==0:
            continue
        
        data=[]
        columns= player.find_all('td')
        name=columns[0].a.get_text()
        year=columns[1].get_text()
        team=columns[2].get_text()
        money=columns[3].get_text()
        money=int(re.sub(r'[^0-9]','',money))
        war=columns[4].get_text()
        
        data.append(name)
        data.append(year)
        data.append(team)
        data.append(money)
        data.append(war)
        writer.writerow(data)
        
            
        print('선수이름 : ',name)
        print('연도 : ',year)
        print('팀이름 : ',team)
        print('연봉 : ',money)
        print('war : ',war)
        print('-'*50)
    f.close()
    
