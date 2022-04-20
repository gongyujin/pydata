from unittest import skip
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
for item in items:
    # 상품명
    name=item.find('span',{'class':'text--title'}).get_text()
    # 금액
    price=item.find('strong',{'class':'text--price_seller'}).get_text()
    price=int(price.replace(',','')) 
    
    
    print(name)
    print(price)