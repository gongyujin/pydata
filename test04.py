# 11번가 > 베스트 > 베스트 500 > 1위-28위 
# 제목, 금액, 링크, 무료배송, 사진을 저장 및 출력하시오. 
import requests
from bs4 import BeautifulSoup

url='https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

icons=soup.find('div',{'class':'best_prd_box'}).ul
li_icons=icons.find_all('li')
for i, li_icon in enumerate(li_icons):
    name=li_icon.find('div',{'class':'pname'}).p.get_text()
    money=li_icon.find('strong',{'class':'sale_price'}).get_text()
    href=li_icon.a['href']
    img=li_icon.find('div',{'class':'img_plot'}).img['src']
    if img.startswith('//'):
        img='https:'+img
    
    print('{}위. {}'.format(i+1,name))
    print('가격 : ',money)
    print('링크 : ',href)
    print('이미지 : ',img)    
        
    free=li_icon.find('div',{'class':'s_flag'})
    if not free.em:
        print('무료배송이 아닙니다.')
        print('-'*60)
        continue

    free=free.get_text().strip()
    print(free)
    print('-'*60)
    
    img_res=requests.get(img)
    img_res.raise_for_status()
    with open('shopping_img_{}.jpg'.format(i+1),'wb') as f:
        f.write(img_res.content)
    
    
    if i >=28:
        break