from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split # train, test
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 확률적경사하강법
# 데이터불러오기 0: red wine, 1: white wine
wine=pd.read_csv('10.mlearn/m0706/wine.csv')
print(wine.columns)

# 로지스틱 회귀 - 정확도를 출력하시오.
data=wine[['alcohol', 'sugar', 'pH']].to_numpy()
label=wine['class'].to_numpy()

# 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 알고리즘 선택
dt=DecisionTreeClassifier(random_state=42)

########### 교차검증 - 분할기 사용
# n_splits: 몇개로 분할할지 결정 ex)10이면 scores가 10개, shuffle: 섞기
splitter=StratifiedKFold(n_splits=10,shuffle=True,random_state=42)
# 훈련 ; scores는 알아서 데이터를 다섯개로 나눠짐
# 훈련: 교차검증함수 cross_validate(알고리즘, 데이터, class)
# fit_time: 훈련시간, score_time: model score값 출력시간, test_score: score정확도
scores=cross_validate(dt,train_data,train_label,cv=splitter) # 딕셔너리 형태
print(scores)
# 정확도 출력
print('train_score : ',np.mean(scores['test_score']))
