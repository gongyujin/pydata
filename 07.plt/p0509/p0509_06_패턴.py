import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

df=pd.read_excel('score.xlsx')

label=df['이름']
values=df['키']


plt.figure(figsize=(8,5))
# bar 패턴그리기 : set_hatch
bar=plt.bar(label,values)
bar[0].set_hatch('//')
bar[1].set_hatch('x')
bar[2].set_hatch('..')

# 그래프 값 넣어주기
for i, txt in enumerate(values):
    # 막대그래프 x:0,1,2,3,4,5,6,7    y:키 
    plt.text(i,values[i]+1.5,txt,ha='center')


# # 막대그래프 - 가로버전 : barh를 하면 가로버전출력
# bar=plt.barh(label,values)
# values1=df['국어']
# values2=df['영어']
# plt.barh(label,values1)
# plt.barh(label,-values2)
plt.ylim(165,210)
plt.show()