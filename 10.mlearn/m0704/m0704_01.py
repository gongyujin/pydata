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
perch_length=np.array(perch_length)
perch_weight=np.array(perch_weight)

perch_length=perch_length.reshape(-1,1) # 2차원배열로 변경

# LinearRegression 회귀 70cm 농어의 무게를 예측하시오!

# 1. 데이터전처리
train_data,test_data,train_label,test_label=train_test_split(perch_length,perch_weight)

# train_data**2 : numpy 배열 => 2차원 데이터 추가
train_data=np.column_stack((train_data**2,train_data))
test_data=np.column_stack((test_data**2,test_data))

# 2. 알고리즘 선택
lr=LinearRegression()

# 3. 실습훈련
lr.fit(train_data,train_label)

# 4. 예측
result1=lr.predict([[50**2,50]]) #1033, 1033
result2=lr.predict([[100**2,100]]) #1033, 1033
predict=lr.predict(test_data)

print('결과1 : ', result1)
print('결과2 : ', result2)

# 5. 정확도 - 예측에서는 정확도 의미가 없음 , score: 알고리즘성능파악을 의미
score1=lr.score(train_data,train_label)
score2=lr.score(test_data,test_label)
print('정확도1 : ', score1)
print('정확도2 : ', score2)

# 6. 오차범위 
mae=mean_absolute_error(test_label,predict) # 실제데이터값, 예측값의 오차를 계산
print('오차범위 : ',mae)

# 구간별 직선을 그림
point=np.arange(15,100) # 15,16,17,....,100까지 배열만들기

print(lr.coef_)
print(lr.intercept_)

# 7. 산점도 그래프
plt.scatter(perch_length,perch_weight)
plt.scatter(50,result1,marker='^')
plt.scatter(100,result2,marker='D')

# x좌표, y좌표 : z=ax+b, 무게= 기울기*15 + y절편
# 기울기 : lr.coef_, y절편 : lr.intercept_
# point, 무게=기울기[0]*point**2+기울기[1]*point+y절편 , point에 15부터 100까지 배열로 다 들어있음
plt.plot(point,lr.coef_[0]*point**2+lr.coef_[1]*point+lr.intercept_)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

