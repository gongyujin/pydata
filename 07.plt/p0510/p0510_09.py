# 나이별 인구현황
# 지역별 인구현황을 원그래프 만들기

from operator import index
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np
import re

# def strchange(temp):
#     result=float(re.sub(r'[^0-9]','',temp))
#     result=result/1000
#     return result

# 백만단위를 천단위로 바꿔줌
df1_m=pd.read_excel('201201_인구현황.xlsx',skiprows=3,index_col='행정기관',usecols='B,E:Y')
df1_w=pd.read_excel('201201_인구현황.xlsx',skiprows=3,index_col='행정기관',usecols='B,AB:AV')
for i in range(len(df1_m)):
    df1_m.iloc[i]=df1_m.iloc[i].str.replace(',','').astype(int)//1000
    df1_w.iloc[i]=df1_w.iloc[i].str.replace(',','').astype(int)//1000
    
label=df1_m.columns
df1_w.columns=df1_m.columns
df1_m=df1_m.iloc[0]
df1_w=df1_w.iloc[0]

# 막대 그래프그리기
plt.barh(label,-df1_m,label='남자')
plt.barh(label,df1_w,label='여자')
plt.title('2012년 연령별 인구현황 그래프')
plt.xlabel('단위:천명',loc='right')
plt.legend()
plt.show()

# ------------------------------------------
# print(df1xx)
# print(df1xy)
# print(df1xx.info())
# print(df1xx[df1xx.columns[1:]])
# df1xx['합계']=df1xx[df1xx.columns[1:]].sum()
# print(df1xx)

