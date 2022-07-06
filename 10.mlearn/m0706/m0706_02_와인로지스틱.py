from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import train_test_split # train, test
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터불러오기 0: red wine, 1: white wine
wine=pd.read_csv('10.mlearn/m0706/wine.csv')
print(wine.columns)

# 로지스틱 회귀 - 정확도를 출력하시오.
data=wine[['alcohol', 'sugar', 'pH']].to_numpy()
label=wine['class'].to_numpy()

# 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 정규화
ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)

# # 알고리즘 선택
# c_lists=[0.01,0.1,1,10,100]
# train_score=[]
# test_score=[]
# for c_list in c_lists:
#     lr=LogisticRegression(C=c_list)
#     # 훈련
#     lr.fit(train_scaled,train_label)

#     # 예측
#     result=lr.predict(test_scaled)

#     # 정답률
#     train_score.append(lr.score(train_scaled,train_label))
#     test_score.append(lr.score(test_scaled,test_label))
# plt.plot(np.log10(c_lists),train_score)
# plt.plot(np.log10(c_lists),test_score)
# plt.show()

lr=LogisticRegression()
# 훈련
lr.fit(train_scaled,train_label)

# 예측
result=lr.predict(test_scaled)
print('결과값 : ', result)

# 정답률
score1= lr.score(train_scaled,train_label)
score2= lr.score(test_scaled,test_label)
print('train score : ',score1)
print('test score : ',score2)