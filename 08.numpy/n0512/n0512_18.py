import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd

# 산점도 그래프
# score.xlsx 파일 국어점수를 읽어와서
# 산점도 크기를 numpy의 랜덤을 이용해서 크기를 설정하시오.

# x=국어점수
# y=영어점수

# size=rand*1000으로 설정하시오

df=pd.read_excel('score.xlsx')

xval=df['국어']
yval=df['영어']

sizes=np.random.rand(len(xval))*1000


plt.scatter(xval,yval,s=sizes,c=sizes,cmap='viridis')
plt.title('국어,영어 산점도 그래프')
plt.xlabel('국어점수')
plt.ylabel('영어점수')
plt.show()

# -----------------------------------
# x=이름
# y=랜덤8개, (60-100)
# 막대그래프
x1=df['이름']
y1=np.random.randint(60,100,8)

plt.bar(x1,y1)
plt.xlabel('이름',color='red')
plt.ylim(50,100)
plt.show()