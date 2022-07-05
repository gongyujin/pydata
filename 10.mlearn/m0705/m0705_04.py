# 붓꽃데이터 품종구별 머신러닝을 구현하시오.
# 1. KNN
# 2. 로지스틱회귀를 사용해서 구현하시오.

# 'SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'
# 5.1 3.8 1.8. 0.5
# 품종을 구별하시오. (확률을 출력할 것)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터 불러오기
df=pd.read_csv('10.mlearn/m0705/iris(150).csv')
data=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].to_numpy()
label=df['Species'].to_numpy()

# 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)


ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)
new_scaled=ss.fit_transform([[5.1,3.8,1.8,0.5]])

# nums=[i for i in range(1,21)]
# train_score=[]
# test_score=[]
# for num in nums:
#     # 알고리즘선택
#     clf=KNeighborsClassifier(n_neighbors=num)
#     # 알고리즘훈련
#     clf.fit(train_scaled,train_label)

#     # 알고리즘 예측
#     result=clf.predict(new_scaled)

#     # 정확도
#     train_score.append(clf.score(train_scaled,train_label))
#     test_score.append(clf.score(test_scaled,test_label))

# plt.plot(nums,train_score)
# plt.plot(nums,test_score)
# plt.show()
    
# 알고리즘선택
clf=KNeighborsClassifier()
# 알고리즘훈련
clf.fit(train_scaled,train_label)

# 알고리즘 예측
result=clf.predict(new_scaled)
proba=clf.predict_proba(new_scaled)
print('예측결과 : ',result)
print('예측결과 proba : ',proba)

# 정확도
score1=clf.score(train_scaled,train_label)
score2=clf.score(test_scaled,test_label)
print('정확도1 : ', score1)
print('정확도2 : ', score2)

