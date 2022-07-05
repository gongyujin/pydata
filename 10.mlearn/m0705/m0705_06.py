from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, SGDClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터불러오기
fish_df=pd.read_csv('10.mlearn/m0705/fish.csv')
# print(fish_df.columns)

data=fish_df[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
label=fish_df['Species'].to_numpy()

# 데이터전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 정규화, 표준화작업 - 손실함수의 값을 줄이는 형태로 구성
ss=StandardScaler()
train_scaled= ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)

# ----------------------------------------------------------------
# 확률적경사하강법 - 머신러닝 알고리즘을 훈련시키는 명령어
# 분류 : 로지스틱손실함수사용, max_iter: 반복횟수
sc=SGDClassifier(loss='log_loss',max_iter=100,random_state=42) # predict, score가 없음, loss='log': logistic 손실함수형태를 쓰겠다는 의미

# 훈련 - 전체 class값이 전송
# 기존의 최적 기울기, 절편은 돌릴때마다 계속 초기화됨
sc.fit(train_scaled,train_label)
# 정확도
score1=sc.score(train_scaled,train_label)
score2=sc.score(test_scaled,test_label)
print('정확도 train : ',score1)
print('정확도 test : ',score2)

# fit함수 : 기울기, 절편을 모두 버리고 다시 훈련시킴
# partial_fit함수 : 기존의 기울기, 절편을 가지고 다시 훈련시킴
sc.partial_fit(train_scaled,train_label)
score1=sc.score(train_scaled,train_label)
score2=sc.score(test_scaled,test_label)
print('정확도2 train : ',score1)
print('정확도2 test : ',score2)

sc.partial_fit(train_scaled,train_label)
score1=sc.score(train_scaled,train_label)
score2=sc.score(test_scaled,test_label)
print('정확도3 train : ',score1)
print('정확도3 test : ',score2)