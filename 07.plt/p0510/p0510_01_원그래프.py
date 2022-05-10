from turtle import color
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 원그래프, 여러개 그래프, 눈금을 2개로 표시

# 원그래프
values = [30,25,20,13,10,2]
# values = [1,2,1,1,2,2]
labels=['python','java','javascript','c#','c++','etc']

x=[1,2,3]
y=[2,4,8]
# plt.plot(x,y) # 선 그래프

# 원그래프 생성
# labels: 외부글자 넣기, autopct: 내부에 % 넣기, startangle: 시작위치, counterclock=False: 시계방향
colors=['#99a5ba','#82ad95','#a898d4','#dee657','#fc5f17','#132452']
plt.figure(figsize=(8,5))
explode=[0.05,0,0,0,0,0]
plt.pie(values,labels=labels,colors=colors,explode=explode,autopct='%.1f%%',startangle=90,counterclock=False) # 원그래프
plt.title('원그래프')
# 범례넣기
plt.legend(loc=(1.1,0.3))
plt.show()