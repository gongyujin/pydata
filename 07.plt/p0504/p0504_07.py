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
# 선-두께,색상,모양,marker ==> 크기, 테두리색,바탕색,모양
plt.plot(x,y,'ro',ms=10,label='평점',linestyle='none')
plt.legend(loc=('lower left'))
plt.title('흥행영화 관객그래프')
plt.xlabel('영화제목',color='r',loc='center')
plt.ylabel('평점',color='b',loc='center')
plt.show()
