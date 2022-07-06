from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split # train, test
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 확률적경사하강법
# 데이터불러오기 0: red wine, 1: white wine
wine=pd.read_csv('10.mlearn/m0706/wine.csv')
print(wine.columns)

# 로지스틱 회귀 - 정확도를 출력하시오.
data=wine[['alcohol', 'sugar', 'pH']].to_numpy()
label=wine['class'].to_numpy()

# 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# min_impurity_decrease 옵션
params={'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005]}

# 그리드서치 적용 - 알고리즘 선택
# n_jobs = -1, cpu의 모든 core를 사용하겠다는 의미
gs=GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)

# 훈련 - 5번 훈련반복
gs.fit(train_data,train_label)

# 훈련 후 가장 성능이 우수한 fit을 dt에 넣음
dt=gs.best_estimator_
# print(dt) # DecisionTreeClassifier(min_impurity_decrease=0.0003, random_state=42)

# 훈련이 성능이 가장 우수한 params의 값을 추출
print(gs.best_params_) # {'min_impurity_decrease': 0.0003}

# 정확도
print('train score : ',dt.score(train_data,train_label))

# 평균 test score
print(gs.cv_results_['mean_test_score'])


