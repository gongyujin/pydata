# 1위 제목
# 금액: xxxx원

from webbrowser import get
import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

url="http://corners.gmarket.co.kr/Bestsellers"
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')

t_div=soup.find('div',{'id':'topPlusItems'})
t2_div=t_div.find_next_sibling('div')
items=t2_div.find_all('li')
for i,item in enumerate(items):
    best_text=item.find('a',{'class':'itemname'}).get_text()
    best_price=item.find('div',{'class':'s-price'}).strong.span.span.get_text()
    print('{}위 {}'.format(i+1,best_text))
    print('금액 : ', best_price)

    icon=item.find('div',{'class':'icon'})
    frees=icon.find_all('img') 

    # if icon.img:
    #     if not icon.img['alt']=='스마일배송':
    #         print(icon.img['alt'])
    # else:
    #     print('무료배송이 아닙니다.')
    # print('-'*20)

    if not frees:
        print('무료배송이 아닙니다.')
    
    for free in frees:
        free1=free['alt']
        if free1=='무료배송':
            print(free1)
    print('-'*20)

# print('1위 ',items[0].find('a',{'class':'itemname'}).get_text())
# print('금액 : ',items[0].find('div',{'class':'s-price'}).strong.span.span.get_text())