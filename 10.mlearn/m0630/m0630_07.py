from sklearn.neighbors import KNeighborsRegressor # knn 회귀
from sklearn.linear_model import LinearRegression # 선형회귀
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 50cm의 농어는 몇 g일까요??
# 1개의 데이터를 산점도 그래프로 출력하시오.

# 1. 데이터 불러오기
perch_length = [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
perch_weight = [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0, 1000.0]

# numpy 타입으로 변형
length=np.array(perch_length)
weight=np.array(perch_weight)

# 2. 데이터 전처리
train_data,test_data,train_label,test_label=\
    train_test_split(length,weight,random_state=42) # 회귀에서는 stratify를 넣지않음

train_data=train_data.reshape(-1,1) # 2차원배열로 변경
test_data=test_data.reshape(-1,1) # 2차원배열로 변경
    
# 3. 알고리즘선택
# knr=KNeighborsRegressor()
lr=LinearRegression()

# 4. 실습훈련
# test데이터가 train보다 정답률이 높으면 과소적합, train이 높으면 과대적합
lr.fit(train_data,train_label)

# LinearRegression -> 기울기, y절편
print("기울기 : ",lr.coef_) 
print("y절편 : ",lr.intercept_) 


# 5. 예측
result0=lr.predict(test_data)
result=lr.predict([[50]])
result2=lr.predict([[100]])
print('test 예측결과 : ', result0)
print('50cm 예측결과 : ',result)
print('100cm 예측결과 : ',result2)

# 6. 정답률, 정확도 (알고리즘 성능비교)
score1=lr.score(train_data,train_label)
score2=lr.score(test_data,test_label)
print('train 정확도 : ', score1)
print('test 정확도 : ', score2)

# 7. 오차범위
mae=mean_absolute_error([[50]],result) # 실제데이터, 예측값을 비교해서 오차값을 구함
mae2=mean_absolute_error([[100]],result2) # 실제데이터, 예측값을 비교해서 오차값을 구함
print('50cm 오차범위 : ',mae)
print('100cm 오차범위 : ',mae2)

# 그래프 그리기
plt.scatter(train_data,train_label)
# 기울기와 y절편을 이용한 선 그래프: y=ax+b
plt.plot([15,100],[15*lr.coef_+lr.intercept_,100*lr.coef_+lr.intercept_])
plt.scatter([[50]],result,marker='^')
plt.scatter([[100]],result2,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

######## 예측은 맞지만 정확도가 떨어짐 #############