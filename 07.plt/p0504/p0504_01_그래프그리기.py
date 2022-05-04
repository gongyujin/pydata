import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('./score.xlsx')
print(df)
print(df['지원번호'])
print(df['국어'])

# 데이터 정보
# x=[1,2,3]
# y=[2,4,8]
x=df['지원번호']
y=df['국어']
z=df['수학']

# plot : 그래프 생성
plt.plot(x,y) # 선 그래프 생성
plt.bar(x,z) # 바 그래프 생성
# 그래프를 보여줌
plt.show()