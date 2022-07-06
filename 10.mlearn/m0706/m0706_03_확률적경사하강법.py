from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import train_test_split # train, test
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LogisticRegression
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

# 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 정규화
ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)

# sc=SGDClassifier(loss='log_loss',random_state=42)
# train_score=[]
# test_score=[]
# classes=np.unique(train_label)
# for idx in range(300):
#     sc.partial_fit(train_scaled,train_label,classes=classes)
#     train_score.append(sc.score(train_scaled,train_label))
#     test_score.append(sc.score(test_scaled,test_label))
    
# plt.plot(train_score)
# plt.plot(test_score)
# plt.show()

sc=SGDClassifier(loss='log_loss',max_iter=250,tol=None,random_state=42)
sc.fit(train_scaled,train_label)
print(sc.score(train_scaled,train_label))
print(sc.score(test_scaled,test_label))