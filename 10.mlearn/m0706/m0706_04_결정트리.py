from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import train_test_split # train, test
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 데이터불러오기 0: red wine, 1: white wine
wine=pd.read_csv('10.mlearn/m0706/wine.csv')
print(wine.columns)

# 로지스틱 회귀 - 정확도를 출력하시오.
data=wine[['alcohol', 'sugar', 'pH']].to_numpy()
label=wine['class'].to_numpy()

# 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)
print(train_data.shape)
# d_lists=[i for i in range(1,21)]
# train_score=[]
# test_score=[]
# # 알고리즘 선택 - 결정트리 분류, max_depth 깊이 : depth를 줄여서 과대적합을 줄일 수 있음
# for d_list in d_lists:
#     dt=DecisionTreeClassifier(max_depth=d_list,random_state=42)
#     # 훈련
#     dt.fit(train_data,train_label)
#     train_score.append(dt.score(train_data,train_label))
#     test_score.append(dt.score(test_data,test_label))
# plt.plot(d_lists,train_score)
# plt.plot(d_lists,test_score)
# plt.show()


dt=DecisionTreeClassifier(max_depth=5,random_state=42)

# 훈련
dt.fit(train_data,train_label)

## 특성에 대한 중요도 - 특성중에 어떤게 가장 중요하게 영향을 미치는지 알려줌
print(dt.feature_importances_)

# 예측
# 정확도
print("train score : ",dt.score(train_data,train_label))
print('test score : ', dt.score(test_data,test_label))

# 그래프 그리기
plt.figure(figsize=(10,7))
# max_depth=1 : 한개만 보여주는 것
plot_tree(dt,max_depth=1,filled=True,feature_names=['alcohol','sugar','pH'])
plt.show()
# 블록색에 따라 class 특성을 나눌수 있음 (filled=True)