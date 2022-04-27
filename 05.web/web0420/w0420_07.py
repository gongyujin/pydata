import re
import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

url="http://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=tv&acode=SRP_SU_0100&arraycategory=&encKeyword=tv"
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')

# 상품평
# 금액
# 평점 4.5이상
# 후기 1000개이상
# 구매수 100개이상
# 상품을 출력하시오.

items=soup.find_all('div',{'class':'itemcard'})
for i,item in enumerate(items):
    # 상품명
    name=item.find('span',{'class':'text--title'}).get_text()
    # 금액
    price=item.find('strong',{'class':'text--price_seller'}).get_text()
    price=int(price.replace(',','')) 
    
    # 평점
    temp_rate=item.find('li',{'class':'item awards'})
    if temp_rate:
        rate=temp_rate.find('span',{'class':'for-a11y'}).get_text()
        rate=float(re.sub(r'[^0-9.]','',rate))
        # 후기
        rate_cnt=item.find('span',{'class':'text--reviewcnt'}).get_text()
        rate_cnt=int(re.sub(r'[^0-9]','',rate_cnt))
        # 구매수
        buy_cnt=item.find('span',{'class':'text--buycnt'}).get_text()
        buy_cnt=int(re.sub(r'[^0-9]','',buy_cnt))
        if rate<4.5 or rate_cnt<1000 or buy_cnt<100:
            continue
    else:
        
        continue
        
    print('{}. 상품명 : {}'.format(i+1,name))
    print('금액 : {}원'.format(price))
    print('평점 : ',rate)
    print('후기 : ',rate_cnt)
    print('구매수 : ',buy_cnt)
    print('-'*40)