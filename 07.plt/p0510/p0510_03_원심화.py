import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

values = [30,25,20,13,10,2]
labels=['python','java','javascript','c#','c++','etc']
colors=['#99a5ba','#82ad95','#a898d4','#dee657','#fc5f17','#132452']
plt.figure(figsize=(8,5))

# 거리 띄우기
explode=[0,0,0,0,0,0]

# 글자를 나타낼때 10이하 숫자는 생략하는 함수
# 30,25,20,13,10,2
def custom_autopct(pct):
    if pct > 10:
        return '{:.1f}%'.format(pct) # return값: '30.0%'
    else:
        return ''                 # return값: ''
  
  
# edgecolor: 테두리색상, linewidth: 테두리두게, width: 도넛형태 (0~1까지, 1보다 작아질수록 두께가 얇아짐)
wedgeprops={'width':0.6,'edgecolor':'w','linewidth':2}  
    
# pie 데이터는 list 형태 : 순차적으로 실행
# pctdistance : 글자거리 (1에 가까울수록 원테두리에 근접)
plt.pie(values,labels=labels,explode=explode,colors=colors,\
    wedgeprops=wedgeprops,autopct=custom_autopct,startangle=90,\
        counterclock=False,pctdistance=0.7)
plt.title('원그래프')
plt.legend(loc=(1.1,0.3))
plt.show()