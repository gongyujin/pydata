from turtle import color
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd

df=pd.read_excel('score.xlsx')

x=df['지원번호']
y=df['국어']

# 그래프 크기 조정 method (그래프 크기를 먼저 설정후 그래프를 그림)
# 해상도 지정 (72dpi-web사이즈, 200dpi,300dpi-인쇄용)
plt.figure(figsize=(10,5),facecolor='y',dpi=72) # 반드시 plt.plot위에 있어야함
plt.bar(x,y,label='국어')
plt.plot(x,df['영어'],label='영어')
plt.plot(x,df['수학'],label='수학')
plt.title('학생성적 그래프')
plt.xlabel('학생번호')
plt.ylabel('점수')
plt.yticks([0,20,40,60,80,100,120])
# ncol 범례를 가로로 출력
plt.legend(loc='lower right',ncol=3)
plt.savefig('학생성적.png',dpi=200) # show위에 있어야함
plt.show()