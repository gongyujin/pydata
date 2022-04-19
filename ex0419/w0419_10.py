# 웹에서 불러오는 숫자는 string이기 때문에 불러와서 float으로 변환시켜줘야함


# 이름, 평점, 날짜 순으로 출력
# 전체 평균 평점

import requests
from bs4 import BeautifulSoup
import soupsieve

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

url='https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')
table=soup.find('table',{'class':'viewList'})
trs=table.find_all('tr')
trs=trs[1:]

rating=[]
for i, tr in enumerate(trs):
    trtxt=tr.find('td',{'class':'title'}).a.get_text()
    trrate=tr.find('div',{'class':'rating_type'}).strong.get_text()
    trdate=tr.find('td',{'class':'num'}).get_text()
    
    
    rating.append(float(trrate))
    print("제목 : {}, 별점 : {}, 날짜 : {}".format(trtxt, trrate, trdate),sep='\t')
print()
    
avg_rate=sum(rating)/len(trs)
print('전체 별점 평균 : {:.2f}'.format(avg_rate))