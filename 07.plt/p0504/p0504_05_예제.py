# score.xlsx 이름, 합계
# 범례 - 성적
# title - 학생성적그래프
# x - 이름
# y - 점수

from cProfile import label
from turtle import color
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15


df=pd.read_excel('score.xlsx',index_col='지원번호')

df['합계']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']

x=df['이름']
y=df['합계']

plt.plot(x,y,marker='o',mec='red',mfc='none',label='성적')
plt.legend(loc=('lower right'))
plt.title('학생성적그래프')
plt.xlabel('이름',color='red')
plt.ylabel('합계',color='green')

plt.show()