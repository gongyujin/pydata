# 대한민국 영화 중에서 관객 수가 가장 많은 상위 8개의 데이터
# 1. 개봉연도별 선그래프를 출력하시오.
# - 선은 red, marker o, 선은 직선
# - x축 눈금표시 2005,2010,2015,2020
# - y축 눈금범위 7,10
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np
data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2016, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}

df = pd.DataFrame(data)
df1=df.sort_values('개봉 연도')
df1=df1.reset_index(drop=True)
x=df1['개봉 연도']
y1=df1['관객 수']
y2=df1['평점']

# plt.plot(x,y1,'ro-')
# for i,(txt1,txt2) in enumerate(zip(x,y1)):
    
#     if i%2==0:
#         plt.text(txt1,txt2+20,txt2,ha='center',fontsize=10)
#     else:
#         plt.text(txt1,txt2-60,txt2,ha='center',fontsize=10)

# plt.title('개봉연도별 관객수 그래프')
# plt.xticks([2005,2010,2015,2020])
# plt.ylim(1000,2000)

# -------------------------------------------------
plt.plot(x,y2,'ro-')

for i,(txt1,txt2) in enumerate(zip(x,y2)):
    # print(i,x[i],y2[i],txt1,txt2)
    if i%2==0:
        plt.text(txt1,txt2+0.1,txt2,ha='center',fontsize=10)
    else:
        plt.text(txt1,txt2-0.2,txt2,ha='center',fontsize=10)

plt.title('개봉연도별 평점 그래프')
plt.xticks([2005,2010,2015,2020])
plt.ylim(7,10)
plt.show()