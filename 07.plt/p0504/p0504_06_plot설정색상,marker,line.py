import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15
# pandas 데이터 정리
df=pd.read_excel('score.xlsx')
x=df['이름']
y=df['국어']
z=df['영어']
# plot.plot : 그래프생성
# linewidth : 선의 두께
# color : b,g,r,pink,gray, #00ff00
# marker : 지점표시(o,x,v)
# linestyle 라인스타일 설정 - none, - , : , -. , --
# plt.plot(x,y,color='r',linewidth=2,marker='o',label='성적',linestyle='--')
# color, marker, linestyle 묶어서 사용가능 bo-- blue, o표시, --선
# plt.plot(x,y,'ro--',linewidth=2,label='성적') # 묶어서 표시가능


# marker 부분 설정
# # markersize: 크기설정, markeredgecolor : 테두리색상, markerfacecolor : 바탕색상
# plt.plot(x,y,label='성적',marker='o',markersize=10, markeredgecolor='red',markerfacecolor='yellow') 

# # ms : markersize, mec : markeredgecolor, mfc : markerfacecolor
# plt.plot(x,y,'bo-',linewidth=2,ms=10, mec='red',mfc='yellow',label='성적')
# alpha : 투명도 조절 (0.0-1.0)
plt.plot(x,y,'ko-',linewidth=2,label='국어')
plt.plot(x,z,'bo-',linewidth=2,label='영어',alpha=0.3)

plt.legend(loc=('upper right'))
plt.title('성적그래프')

plt.xlabel('이름',loc='center')
plt.ylabel('국어점수',loc='center')


# 그래프 그려줌
plt.show()

