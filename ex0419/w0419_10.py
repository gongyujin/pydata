# 웹에서 불러오는 숫자는 string이기 때문에 불러와서 float으로 변환시켜줘야함


# 이름, 평점, 날짜 순으로 출력
# 전체 평균 평점

import requests
from bs4 import BeautifulSoup
import soupsieve

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}


# res=requests.get(url,headers=headers)
# soup=BeautifulSoup(res.text,'lxml')
# table=soup.find('table',{'class':'viewList'})
# trs=table.find_all('tr')
# trs=trs[1:]

# all_rate=0
# for i, tr in enumerate(trs):
#     trtxt=tr.find('td',{'class':'title'}).a.get_text()
#     trrate=tr.find('div',{'class':'rating_type'}).strong.get_text()
#     trdate=tr.find('td',{'class':'num'}).get_text()
    
    
#     all_rate+=float(trrate)
#     print("제목 : {}, 별점 : {}, 날짜 : {}".format(trtxt, trrate, trdate),sep='\t')
# print()
    
# avg_rate=all_rate/len(trs)
# print('전체 별점 평균 : {:.2f}'.format(avg_rate))


## 강사님 코드
# find, find_all은 아무것도 없을때 none으로 프로그램이 계속 구동됨
# none에서 get_text()를 하게 되면 error 발생

# 전체 페이지 for문
all_rate=0 # 전체 평균 변수
page_count=5
for i in range(1,page_count+1):
    url='https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu'+'&page='+str(i)
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')
    
    web_table=soup.find('table',{'class':'viewList'})
    cartoons=web_table.find_all('tr')
    for cartoon in cartoons:
        car_title=cartoon.find('td',{'class':'title'})
        if not car_title: # 글자가 없을 때 false로 인식
            continue
        car_rate=cartoon.find('div',{'class':'rating_type'})
        temp_rate=car_rate.strong.get_text()
        all_rate+=float(temp_rate)
        car_date=cartoon.find('td',{'class':'num'})
        print("제목 : ",car_title.a.get_text()) # 제목
        print("평점 : ",temp_rate) # 별점
        print("날짜 : ",car_date.get_text()) # 날짜
        print('-'*20)
        
print('전체 별점 평균 : {:.2f}'.format(all_rate/((len(cartoons)-1)*page_count)))
print()