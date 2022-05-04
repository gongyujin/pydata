import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

# 영화, 관객수를 이용해서 그래프 그리기
df=pd.read_excel('movie.xlsx')

x=df['영화']
y=df['평점']
plt.plot(x,y,'ro:',label='평점')
plt.legend(loc=('upper right'))
plt.title('흥행영화 관객그래프')
plt.xlabel('영화제목')
plt.ylabel('평점')
plt.show()
