from unittest import skip
import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

url="https://www.goodchoice.kr/product/result?keyword=%EC%98%A4%EC%85%98%EB%B7%B0"
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')

# 평점 9.5이상이면서 상품평 500개 이상인 것만 출력
# 제목 : 제이앤파크 호텔
# 평점 : 9.5
# 상품평 : 126

items=soup.find_all('li',{'class':'list_4'})
count=1
for i,item in enumerate(items):
    
    item_url=item.find('a')['href']
    # name=item.find('img',{'class':'lazy'})['alt'] # 숙소명 img 태그안에 찾기
    rate=float(item.find('p',{'class':'score'}).span.em.get_text())

    # span태그 다음요소 선택, 좌우공백제거
    rate_cnt=item.find('p',{'class':'score'}).span.next_sibling.strip()
    # (184) -> 첫번째자리에서 마지막앞자리까지 슬라이싱 : 184
    rate_cnt=int(rate_cnt[1:-1])
    if rate<9.5 or rate_cnt<500:
        continue
    
    name=item.find('div',{'class':'name'}).strong
    name2=item.find('div',{'class':'name'}).strong.find('div',{'class':'badge'})
    if name2:
        re_title=name2.next_sibling.strip()
    else:
        re_title=name.get_text().strip()
        
    print('{}. 숙소명 : {}'.format(count,re_title))
    print('평점 : ',rate)
    print('상품평 : ',rate_cnt)
    print('바로가기 링크 : ',item_url)
    print('-'*20)
    count+=1
    
