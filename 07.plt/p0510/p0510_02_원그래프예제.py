# score 5명의 학생의 국어성적을 원그래프로 출력하시오.
# 테두리 흰색, 도넛형태 꾸미기
# 10이하는 생략이라는 글자

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df=pd.read_excel('score.xlsx')
df=df[:5].sort_values('국어',ascending=False)
values=df['국어']
labels=df['이름']

explode=[0.05,0,0,0,0]
colors=['#99a5ba','#82ad95','#a898d4','#dee657','#fc5f17']

def custom_autopact(pct):
    if pct>10:
        return '{:.1f}%'.format(pct)
    else:
        return '생략'
    # return '{:.1f}%'.format(pct) if pct>10 else '생략'

wedgeprops={'width':0.6,'edgecolor':'w','linewidth':2}
plt.figure(figsize=(8,5))
plt.pie(values,labels=labels,explode=explode,colors=colors,\
    wedgeprops=wedgeprops,autopct=custom_autopact,startangle=90,\
        counterclock=False,pctdistance=0.7)
plt.title('국어성적 원그래프')
plt.legend(loc=(1.1,0.3))
plt.show()