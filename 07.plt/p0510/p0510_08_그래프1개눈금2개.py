import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df=pd.read_excel('score.xlsx')

x=df['이름']
y=df['키']
# y=[1100,1200,1500,1600,1000,1300,1100,1400]
z=df['국어']

# 여러개 그래프
fig,ax1=plt.subplots()
ax1.set_ylabel('키')
ax1.set_ylim(160,210)
ax1.plot(x,y,'o-')

# ax1과 x축을 동일한 것으로 사용
ax2=ax1.twinx()
ax2.set_ylabel('국어')
ax2.set_ylim(10,110)
ax2.plot(x,z,'x--')

for i, (val1,val2) in enumerate(zip(z,y)):
    ax2.text(i,val1+2,val1,ha='center')
    
    if (i==0) or (i==2):
        ax1.text(i,val2-5,val2,ha='center')
    else:
        ax1.text(i,val2+2,val2,ha='center')
        
# 1개 그래프일때
# plt.plot(x,y)
# plt.plot(x,z)

plt.show()