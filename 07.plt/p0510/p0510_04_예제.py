# stu1000 -> 학년별 비율을 원그래프로 출력하시오.
# 1학년
# 2학년
# 3학년
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df=pd.read_excel('stu1000.xlsx')
print(df)
df2=df.groupby('학년').size() #series

# list타입의 1,2,3학년 데이터값
df3=list(df2) 

# for i, (rank,cnt) in enumerate(df2.iteritems()):
#     print(i,rank,cnt)
values=df3
labels =['1학년','2학년','3학년']
colors =['#ffebb5','#ffc0b5','#dbffb5']
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}

plt.figure(figsize=(8,5))
explode = [0,0,0]
plt.pie(values,labels=labels,colors=colors, \
    wedgeprops=wedgeprops,explode=explode,autopct='%.1f%%',\
        pctdistance=0.7,startangle=90,counterclock=False)
plt.title('학년별 인원 그래프')
# 범례넣기 - title을 하면 범례에 제목입력
plt.legend(loc=(1.1,0.3),title='학년별 인원')
plt.show()