# iris(150).csv
# 특정데이터를 입력하여서 붓꽃 데이터의 품종을
# 분류하는 프로그램을 구축하시오.
# 'SepalLength','SepalWidth','PetalLength','PetalWidth','Species'

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df=pd.read_csv('10.mlearn/m0629/iris(150).csv')

# 1. 데이터를 가져오기
data=df[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
label=df[['Species']]


# 2. 데이터 전처리
# train_data,train_label,test_data,test_label
train_data,test_data,train_label,test_label\
    =train_test_split(data,label,test_size=0.3,stratify=label,random_state=42)

# # numpy 타입변경
# data_numpy= np.array(data)
# index=np.arange(150)
# np.random.shuffle(index)
# train_data=data_numpy[index[:120]]



# 3. 알고리즘선택 : knn
clf=KNeighborsClassifier()

# 4. 알고리즘 실습훈련
clf.n_neighbors=4 # default값 = 5
clf.fit(train_data,train_label)

# # 5. 예측
# SepalLength=float(input('SepalLength를 입력하세요.>> '))
# SepalWidth=float(input('SepalWidth 입력하세요.>> '))
# PetalLength=float(input('PetalLength 입력하세요.>> '))
# PetalWidth=float(input('PetalWidth 입력하세요.>> '))
# example=[[SepalLength,SepalWidth,PetalLength,PetalWidth]]
# result=clf.predict(example)
# print('결과 : ', result)
result=clf.predict(test_data)
print('결과 : ', result)

# 6. 정답률
score1=clf.score(test_data,test_label)
score2=clf.score(train_data,train_label)
print('test 정답률 : ',score1)
print('train 정답률 : ',score2) # 더 높아야함