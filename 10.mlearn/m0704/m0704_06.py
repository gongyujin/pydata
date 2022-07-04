from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기, 분리하기 : pandas 사용 ; read_csv, to_csv
# 데이터의 배열형태 변경 : numpy ; to_numpy, array, column_stact, concatenate
df=pd.read_csv('10.mlearn/m0704/iris(150).csv')

# data 2차원 numpy 배열로 만들기
data=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].to_numpy()
label=df['Species'].to_numpy()

# 1. 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label)

# 2. 알고리즘 선택
clf=KNeighborsClassifier()

# 3. 실습훈련
clf.fit(train_data,train_label)

# 4. 예측 : 5.2 3.4 4.8 0.2
result=clf.predict([[5.2,3.4,4.8,0.2]])
print('예측결과 (5.2,3.4,4.8,0.2) : ',result)

# 5. 정답률
score=clf.score(test_data,test_label)
print('정답률 : ',score)