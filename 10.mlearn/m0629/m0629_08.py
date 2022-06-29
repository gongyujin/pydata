from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 1. 데이터 불러오기
train_csv=pd.read_csv('10.mlearn/mnist/train.csv',header=None)
test_csv=pd.read_csv('10.mlearn/mnist/t10k.csv',header=None)

# # 2. 데이터 전처리
# 이미지 데이터일 경우 0-1까지의 수로 표시
# map 함수

def func(a):
    output=[]
    for i in a:
        output.append(float(i)/256)
    return output

# data만 map으로 재분배해줌
train_data=list(map(func,train_csv.iloc[:,1:].values)) #0-255숫자를 배분해서 넣어둠
test_data=list(map(func,test_csv.iloc[:,1:].values))
train_label=train_csv[0].values
test_label=test_csv[0].values

# 3. 알고리즘 선택
clf = KNeighborsClassifier()

# 4. 실습훈련
clf.fit(train_data,train_label)

# 5. 예측
result=clf.predict(test_data)
print('결과값 : ', result)

# 6. 정답률
score1=clf.score(test_data,test_label)
score2=clf.score(train_data,train_label)
print('test 정답률 : ',score1)
print('train 정답률 : ',score2)