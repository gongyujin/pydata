from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split # train, test
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터불러오기 0: red wine, 1: white wine
wine=pd.read_csv('10.mlearn/m0706/wine.csv')
print(wine.columns)
data=wine[['alcohol', 'sugar', 'pH']].to_numpy()
label=wine['class'].to_numpy()

# 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 알고리즘선택 : n_jobs - cpu core개수를 몇개 사용할지 정함 (-1은 모든 core를 사용하겠다는 의미)
# 랜덤포레스트 : 결정트리사용 디폴트 10개 사용, n_estimators=100 로 변경가능
rf= RandomForestClassifier(random_state=42,n_jobs=-1)

# 교차검증훈련
# return_train_score= True : train score가 출력됨
scores=cross_validate(rf,train_data,train_label, n_jobs=-1, return_train_score=True)

print('train_score 평균 : ',np.mean(scores['train_score']))
print('test_score 평균 : ',np.mean(scores['test_score']))

# 정확도
rf.fit(train_data,train_label)
print('test_data score : ',rf.score(test_data,test_label))

# 특성의 중요도
print('특성의 중요도 : ',rf.feature_importances_)
