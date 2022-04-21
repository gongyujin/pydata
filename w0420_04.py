from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import re
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

for i in range(1,6):
    url='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page='+str(i)+'&rocketAll=false&searchIndexingToken=1=6&backgroundColor='

    res=requests.get(url,headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'lxml')


    # 정규표현식가지고 검색
    # items=soup.find_all('li',{'class':re.compile('^search-product')})
    items=soup.find_all('li',{'class':'search-product'})
    # print("item 개수 : ",len(items))
    # print(items)
    ad_count=0
    item_ct=0
    for idx, item in enumerate(items):
        if 'search-product__ad-badge' in item['class']:
            ad_count+=1
            continue
        
        # 4.5이상, 100이상일때 출력 : 제품명, 가격, 링크
        # 평점
        rate=item.find('em',{'class':'rating'})
        if not rate:
            continue
        
        rate1=rate.get_text()
        rate2=float(rate1)
        # 상품평
        rate_cnt=item.find('span',{'class':'rating-total-count'}).get_text()
        # (150) -> 문자에서 첫번째부터 마지막 전까지 슬라이싱
        rate_cnt2=int(rate_cnt[1:-1])
        if rate2>=4.5 and rate_cnt2 >= 200:
            
            # 제품명
            product_name=item.find('div',{'class':'name'}).get_text()
            # # 제품명에 Apple이라는 단어가 포함되어 있는지 확인
            if "Apple" in product_name:
                continue
            
            print('제품명 : {}'.format(product_name))
            print('평점 : ',rate2)
            print('상품평 개수 : ',rate_cnt2)
            # 가격
            print('가격 : ',item.find('strong',{'class':'price-value'}).get_text())
            # 링크
            print('링크 : ','https://www.coupang.com'+item.a['href'])
            print('-'*20)
            item_ct+=1
            
    print('광고상품 개수 : ',ad_count)
    print('제품 개수 : ',item_ct)
    print()