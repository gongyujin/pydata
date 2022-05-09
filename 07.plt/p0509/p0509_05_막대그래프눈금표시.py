# 막대그래프
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

df=pd.read_excel('score.xlsx')
x=df['이름']
y=df['키']
# 그래프를 x축으로 넓혀줌
plt.figure(figsize=(10,5))
# 막대그래프 그리기: plt.bar, 그래프두께조절 : width, 투명도조절 : alpha
# plt.bar(x,y,width=0.5)
plt.bar(x,y,width=0.2,alpha=0.5)

for i,txt in enumerate(y):
    plt.text(x[i],y[i]+1,txt,ha='center')
    
# # x좌표 글자 기울기
# plt.xticks(x,rotation=45)
# plt.yticks([170,180,190,200,210])
# y축 그래프를 제한
plt.ylim(160, 210)
plt.show()