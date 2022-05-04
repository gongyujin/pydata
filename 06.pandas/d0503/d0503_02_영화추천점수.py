# 1. 다음영화 웹스크래핑을 함
# 2016부터 2021년 영화를 가져옴 - 5개 영화 가져오기
# 영화제목, 평점, 개봉일, 누적인원

# 2. pandas로 변환
# 추천점수 컬럼을 만듬
# (관객수*평점)/100

# 3. 추천점수가 높은 순으로 출력하시오.

import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

filename='2016-2021 movie.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')
writer=csv.writer(f)

title='영화번호,영화제목,평점,개봉일,관객수'
title=title.split(',')
writer.writerow(title)

count=1
for year in range(2016,2022):

    url='https://search.daum.net/search?w=tot&q='+str(year)+'%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')

    movie_lists=soup.find('ol',{'class':'type_plural list_exact movie_list'})
    movies=movie_lists.find_all('li')
    for i, movie in enumerate(movies):
        movie1=movie.find('div',{'class':'wrap_cont cont_type2'})
        
        name=movie1.a.get_text()
        rank=float(movie1.find('dd',{'class':'score'}).em.get_text())
        oday=movie1.find('dl',{'class':'dl_comm'}).find_next_sibling('dl').dd.get_text().strip()
        hcount=movie1.find('dl',{'class':'dl_comm'}).find_next_sibling('dl').find_next_sibling('dl').find_next_sibling('dl').dd.get_text()
        hcount=re.sub(r'[^0-9,]','',hcount)
        print('제목 : ',name)
        print('평점 : ',rank)
        print('개봉일 : ',oday)
        print('누적관객수 : ',hcount)
        print('-'*50)
        data=[]
        
        data.append(count)
        data.append(name)
        data.append(rank)
        data.append(oday)
        data.append(hcount)
        writer.writerow(data)
        
        count+=1
        
        if i >=4:
            break

f.close()

df=pd.read_csv('2016-2021 movie.csv',index_col='영화번호')

df['추천점수']=((df['관객수'].str.replace(',','').astype(int))*df['평점'])/100

print(df.sort_values('추천점수',ascending=False))
