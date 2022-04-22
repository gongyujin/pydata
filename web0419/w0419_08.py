import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,"lxml")


rankall=soup.find('div',{'class':'col_inner'})
# 10개의 li태그를 리스트 형태로 반환
cartoons=rankall.find_all('a',{'class':'title'}) # 리스트 형태
for i,cartoon in enumerate(cartoons):
    print("{:2d} 번째 : {}".format(i+1,cartoon.get_text()))
    print("바로가기 : ","https://comic.naver.com"+cartoon['href'])



# # 10개의 인기웹툰 li태그를 가져옴 (li태그 10개 담겨져 있음)
# rankall=soup.find('ol',{'id':'realTimeRankFavorite'})
# # 10개의 li태그를 리스트 형태로 반환
# cartoons=rankall.find_all('li') # 리스트 형태
# for i,cartoon in enumerate(cartoons):
#     print("{:2d} 위 : {}".format(i+1,cartoon.a.get_text()))
#     print("바로가기 : ","https://comic.naver.com"+cartoon.a['href'])
# print(rankall)
# print(cartoons)

# rank2=soup.find('li',{'class':'rank02'})
# 현재기준 바로 다음 검색
# print(rank1.next_sibling.next_sibling) # 엔터키가 적용되어 있는거는 그다음줄에 있는 것으로 여겨서 next_sibling을 두번해줘야함
# print(rank2.previous_sibling.previous_sibling)

#find_next_sibling은 현재기준부터 li를 찾을때까지 검색
# print(rank1.find_next_sibling('li')) 
# 현재기준 이전에서 li를 찾을때까지 검색
# print(rank2.find_previous_sibling('li'))

