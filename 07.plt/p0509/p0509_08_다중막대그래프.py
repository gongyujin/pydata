import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

# 다중막대 그리기
df=pd.read_excel('score.xlsx')

# x=[0,1,2,3,4,5,6,7] ==> ['강나래','강태원',....'']
# x=df['이름']

y1=df['국어']
y2=df['영어']
y3=df['수학']

# 막대그래프에 데이터값을 표시
# plt.text(0,90,100,ha='center')
# for i,txt in enumerate(y1):
#     plt.text(i-0.2,y1[i]+2,txt,ha='center')

# numpy를 생성후 -0.25 계산실행
x=np.arange(8)

plt.figure(figsize=(8,5))
plt.bar(x-0.25,y1,label='국어',width=0.25)
plt.bar(x,y2,label='영어',width=0.25)
plt.bar(x+0.25,y3,label='수학',width=0.25)

# 눈금표시 0부터 110으로 변경
plt.ylim(0,110)
plt.xticks(x,df['이름']) 
plt.legend(ncol=3)
plt.show()

# # # x list를 만들려면
# # x=[0,1,2,3,4,5,6,7]
# x=[]
# for i in range(8):
#     x.append(i)
# print(x)

# # # y list를 만들려면
# y=[]
# for i in x:
#     y.append(i-0.25)
# print(y)
