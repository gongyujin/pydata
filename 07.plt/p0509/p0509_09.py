# stu1000
# 합계점수가 높은 1학년 5명 출력
# 국어,영어,수학,과학 그래프 출력하시오.
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=12
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
import numpy as np

df=pd.read_excel('stu1000.xlsx')

# 1.합계컬럼 생성
df['합계']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']

# 2.
# 1학년이면서 좀수가 높은 순으로 정렬
# 합계점수 역순정렬, 학년 순차정렬 sort
find_df=df.sort_values(['학년','합계'],ascending=[True,False]).head(5)
print(find_df)
# df1=(df[df['학년']==1]).sort_values('합계',ascending=False)[0:5]
# print(df1)

# 3.각 컬럼 데이터 생성
name=find_df['이름']
y1=find_df['국어']
y2=find_df['영어']
y3=find_df['수학']
y4=find_df['과학']
y5=find_df['사회']

# 4. 다중막대그래프 그리기
x=np.arange(5)*2

plt.figure(figsize=(10,5))

plt.bar(x-0.5,y1,label='국어',width=0.25)
plt.bar(x-0.25,y2,label='영어',width=0.25)
plt.bar(x,y3,label='수학',width=0.25)
plt.bar(x+0.25,y4,label='과학',width=0.25)
plt.bar(x+0.5,y5,label='사회',width=0.25)

for i,y1,y2,y3,y4,y5 in zip(x,y1,y2,y3,y4,y5):
    plt.text(i-0.5,y1+1,y1,ha='center')
    plt.text(i-0.25,y2+1,y2,ha='center')
    plt.text(i,y3+1,y3,ha='center')
    plt.text(i+0.25,y4+1,y4,ha='center')
    plt.text(i+0.5,y5+1,y5,ha='center')

plt.ylim(60,110)
plt.xticks(x,name)
plt.legend(loc='upper right',ncol=5)
plt.show()