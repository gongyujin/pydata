from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from scipy.special import expit
import matplotlib.pyplot as plt

# [ 도미 ] =1 ,35개
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0,
33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0,
610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# [ 빙어 ] =0 ,14개
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

length=bream_length+smelt_length # 49개
weight=bream_weight+smelt_weight

data=np.column_stack((length,weight))
label=np.concatenate((['도미']*35,['빙어']*14))

# 분리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 정규화

ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)
new_scaled1=ss.fit_transform([[30,600]])
new_scaled2=ss.fit_transform([[25,150]])

# 알고리즘선택
lr=LogisticRegression()

# 훈련
lr.fit(train_scaled,train_label)

# 예측
result=lr.predict(new_scaled1)
result2=lr.predict(new_scaled2)
print('[30,600] 분류 : ',result)
print('[25,150] 분류: ',result2)
print('-'*50)
print(lr.predict(test_scaled[:5]))
proba=lr.predict_proba(test_scaled[:5])
print(proba)

# 정답률
score=lr.score(test_scaled,test_label)
print('test 정답률 : ',score)
score2=lr.score(train_scaled,train_label)
print('train 정답률 : ',score2)

# z값
decisions=lr.decision_function(test_scaled[:5])
print(decisions)

# 시그모이드 함수
print(expit(decisions))

# 산점도
plt.scatter(length,weight)
plt.scatter(30,600,marker='^')
plt.scatter(25,150,marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()