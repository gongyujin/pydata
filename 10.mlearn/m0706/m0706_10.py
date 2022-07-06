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

# 결정트리알고리즘 그리드서치를 사용
# params : 3개를 사용해서 최종 score 구하시오.
params={
    'min_impurity_decrease':np.arange(0.0001,0.001,0.0001),
    'max_depth':range(5,20,1),
    'min_samples_split':range(2,100,10)
}

train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

gs=GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)

gs.fit(train_data,train_label)

# 최고성능 decisiontreeclassifier
dt=gs.best_estimator_
print('train score : ',dt.score(train_data,train_label))
print('test score : ',dt.score(test_data,test_label))

# 평균 test score
print(gs.cv_results_['mean_test_score'])
