import re
import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

# 년도별 역대관객순위 5위 가져오기
for year in range(2017,2022):
    

    url="https://search.daum.net/search?w=tot&q="+str(year)+"%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')

    # images=soup.find_all('img',{'class':'thumb_img'})
    # for i,image in enumerate(images):
    #     img_url = image['src']
    #     # startswith 함수 : 해당문자로 시작하는지 확인
    #     if img_url.startswith('//'):
    #         img_url="https:"+img_url
    #     print(img_url)
            
    #     # 이미지 링크를 가지고
    #     img_res=requests.get(img_url)
    #     img_res.raise_for_status()
        
    #     # with open('aaa.html','w',encoding='utf-8')
    #     # 문자저장시 인코딩이 필요
    #     with open('movie2021_{}.jpg'.format(i+1),'wb') as f:
    #         # requests에서 리턴하는 3가지 - status_code-상태, text-문자, content-파일
    #         # f.write(res.text) # 문자일때
    #         f.write(img_res.content)
        
    #     # 상위 5개 이미지만 출력
    #     if i>=4:
    #         break

    # 역대 관객순위 30위 li의 상위 ol찾기
    movie_ol=soup.find('ol',{'class':'type_plural list_exact movie_list'})
    # 역대 관객순위 30개
    movies=movie_ol.find_all('li')
    for i,movie in enumerate(movies):
        # 제목
        name=movie.find('a',{'class':'tit_main'}).get_text()
        # 평점 (float형변환)
        rate=float(movie.find('em',{'class':'rate'}).get_text())
        print('영화제목 : ',name)
        print('평점 : ',rate)
        
        # 누적 관객수 출력, s_cnt 마지막 list를 출력
        s_cnt = movie.find_all('dd',{'class':'cont'})
        ss_cnt=s_cnt[len(s_cnt)-1].get_text()
        print('누적 : ',ss_cnt)
        
        # 이미지 링크, url주소가 https: 없으면 추가
        s_img=movie.find('img',{'class':'thumb_img'})['src']
        if s_img.startswith('//'):
            s_img="https:"+s_img
        # 영화링크 출력
        s_link = movie.find('div',{'class':'info_tit'}).a['href']
        print('링크 : ','https://search.daum.net/search'+s_link)
        
        print('-'*50)
        
        # 영화포스터 이미지 파일저장
        s_img_res=requests.get(s_img)
        s_img_res.raise_for_status() # 데이터없을시 종료
        # 파일저장 (파일이기 때문에 인코딩할 필요가 없음)
        with open('movie{}_{}.jpg'.format(year,i+1),'wb') as f:
            f.write(s_img_res.content)
        
        # 상위 5개 이미지만 출력, 상위 10개 출력하라면 9, 30위까지 출력가능
        if i>=4:
            break