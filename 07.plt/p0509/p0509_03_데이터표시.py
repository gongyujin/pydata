from turtle import color
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

df=pd.read_excel('score.xlsx')
x=df['지원번호']
y=df['국어']
# ro--: r 색상, o marker, -- linestyle
plt.plot(x,y,'o-',label='국어')
plt.title('학생성적 그래프')
plt.xticks([0,1,2,3,4,5,6,7])

# 그래프에 점수표시
# i=[0,1,2,3,4,5,6,7]
for i, txt in enumerate(y):
    plt.text(x[i],y[i]+2,txt,ha='center')
# plt.text(6.5,y[7]-2,100,ha='center')


plt.show()