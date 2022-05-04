import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15 # 상단제목 글자 15크기 변환
matplotlib.rcParams['axes.unicode_minus']=False # 눈금 -표시 처리
# matplotlib.rcParams['font.family']='Apple Gothic' # 맥사용시


df=pd.read_excel('./score.xlsx')
print(df['지원번호'])
print(df['국어'])

# 데이터 정보
# x=[1,2,3]
# y=[-2,4,8]
x=df['이름'] # 리스트형태로 넘어옴
y=df['국어']

plt.plot(x,y)
# 상단 제목출력 - 영문은 가능, 단 한글 사용시 에러발생
plt.title('GRAPH그래프')
plt.show()