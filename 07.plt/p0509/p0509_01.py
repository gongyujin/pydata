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
y=df['키']

# x=[1,2,3]
# y=[-2,-4,8]

# ro-- : r color, o marker, -- linestyle
plt.plot(x,y,marker='x',linestyle=':',label='키')
plt.title('학생 그래프')
plt.xlabel('학생번호',color='red')
plt.ylabel('키',color='g')
# plt.xticks([1,2,3,4,5,6,7,8])
# plt.yticks([0,100,200])
plt.grid(axis='y')

plt.legend()
plt.show()