from sklearn.neighbors import KNeighborsRegressor # knn 회귀
from sklearn.linear_model import Lasso, LinearRegression, Ridge # 선형회귀
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 선형회귀 - 다중회귀
# length, height, width => length**2,length,height**2,height,width**2,width
# 30.4, 8.89, 4.22 무게를 예측하시오.
# degree 5
# linearRegression 알고리즘 사용할것 - > Ridge()의 alpha값을 사용하여
# 최상의 알고리즘을 구현하시오.

# 1. 데이터 불러오기
df = pd.read_csv('10.mlearn/m0630/perch_full2.csv')
# print(df.columns)


# 2. 데이터 전처리
perch_full=df[['length',' height',' width']]
perch_full=perch_full.to_numpy()
weight=df['weight']
weight=weight.to_numpy()

train_data,test_data,train_label,test_label=train_test_split(perch_full,weight,random_state=42)

poly=PolynomialFeatures(degree=5,include_bias=False)
poly.fit(train_data)
train_poly=poly.transform(train_data)
test_poly=poly.transform(test_data)
new_poly=poly.transform([[30.4,8.89,4.22]])

# 정규화
ss=StandardScaler()
ss.fit(train_poly)
train_scaled=ss.transform(train_poly)
test_scaled=ss.transform(test_poly)
new_scaled=ss.transform(new_poly)

# # 3. 알고리즘 선택
# lr=LinearRegression()
# alpha_list=[0.01,0.1,1,10,100]

# train_score=[]
# test_score=[]
# for list in alpha_list:
#     ridge=Lasso(alpha=list)
#     ridge.fit(train_scaled,train_label)
#     train_score.append(ridge.score(train_scaled,train_label))
#     test_score.append(ridge.score(test_scaled,test_label))
    
    
# # 선그래프 그리고 선택
# plt.plot(np.log10(alpha_list),np.log10(train_score))
# plt.plot(np.log10(alpha_list),np.log10(test_score))
# plt.xlabel('alpha')
# plt.ylabel('scaled')
# plt.show()
    
# 4. 실습훈련
# 특성값을 제거해서 규제
lasso=Lasso(alpha=10)
lasso.fit(train_scaled,train_label)

# 5. 예측값
result=lasso.predict(new_scaled)
predict=lasso.predict(test_scaled)
print('new 예측값 : ', result)

# 6. 정확도확인
score1=lasso.score(train_scaled,train_label)
score2=lasso.score(test_scaled,test_label)
print('score1 : ',score1)
print('score2 : ',score2)

print('0인 특성값 : ',np.sum(lasso.coef_ ==0 ))
# 특성값을 늘리는 이유는 정확도를 높이기 위해서 늘림, 단 차수를 높이고 특성값이 0인 부분을 많이 넣음으로써 차수를 다시 낮춤 => 이상한 현상

# 7. 오차범위
mae=mean_absolute_error(test_label,predict)
print('오차범위 : ',mae)