from sklearn.neighbors import KNeighborsRegressor # knn 회귀
from sklearn.linear_model import LinearRegression, Ridge # 선형회귀
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 선형회귀 - 다중회귀
# length, height, width => length**2,length,height**2,height,width**2,width
df = pd.read_csv('10.mlearn/m0630/perch_full.csv')
# 무게 데이터
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 
    110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 
    130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 
    197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 
    514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 
    820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 
    1000.0, 1000.0]
)

# # 2개의 데이터 1개의 perch_full2.csv로 저장하시오.
# df['weight']=perch_weight
# df.to_csv('10.mlearn/m0630/perch_full2.csv',encoding='utf-8-sig',index=False)

# df=pd.read_csv('10.mlearn/m0630/perch_full2.csv')
# print(df)

# numpy배열타입으로 변경, pd.to_numpy();판다스에서 numpy로 바꾸는 형태, np.array(); numpy를 다른 형태로 바꾸는 것
perch_full=df.to_numpy()
# perch_full=np.array(df)
# print(type(perch_full))

# 1. 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(perch_full,perch_weight,random_state=42)
# 다중회귀 - 다항회귀
# train_data=np.column_stack((train_data**3,train_data**2,train_data))
# degree는 몇차 방정식인지 기입, default는 2차방정식(degree=2)
poly=PolynomialFeatures(degree=5,include_bias=False) 
##### degree=5로 변경시 train predict는 거의 100프로 test predict는 마이너스 값을 가짐 ==> 과대적합이라고 볼 수 있음; 규제필요함


poly.fit(train_data)
train_poly=poly.transform(train_data) # 2차원방정식으로 변형
# poly.fit_transform(train_data)
test_poly=poly.transform(test_data)

# print(poly.get_feature_names()) # 어떻게 다차원식으로 변경되었는지 볼 수 있음
# print(train_data.shape)
# print(train_poly.shape)

new_poly=poly.transform([[30.4,8.89,4.22]])

# 정규화, 표준화작업
ss=StandardScaler()
ss.fit(train_poly)
train_scaled=ss.transform(train_poly)
test_scaled=ss.transform(test_poly)
new_scaled=ss.transform(new_poly)

# 2. 알고리즘 선택 : 규제 - 릿지회귀 alpha값 확인
# 규제 - 릿지회귀
# # Ridge규제 : degree를 규제해줌
# lr=LinearRegression()

# train_score=[]
# test_score=[]
# alpha_list=[0.01,0.1,1,10,100]
# # alpha(규제강도) : alpha의 default값은 1, 낮을수록 규제가 낮아지고 높을수록 규제가 높아짐
# for list in alpha_list:
#     ridge=Ridge(alpha=list) 

#     # print(df.describe())

#     # 3. 실습훈련
#     ridge.fit(train_scaled,train_label)
#     # print(ridge.coef_,ridge.intercept_)

#     # 5. 정확도체크
#     train_score.append(ridge.score(train_scaled,train_label))
#     test_score.append(ridge.score(test_scaled,test_label))
    
    
# plt.plot(np.log10(alpha_list),train_score)
# plt.plot(np.log10(alpha_list),test_score)
# plt.xlabel('alpha')
# plt.ylabel('score')
# plt.show()

# 릿지회귀 : 기울기의 제곱을 규제 - L2규제
ridge=Ridge(alpha=0.1) 
# 3. 실습훈련
ridge.fit(train_scaled,train_label)

# 4. 예측: 30.4   8.89   4.22
result=ridge.predict(new_scaled)
predict=ridge.predict(test_scaled)


# 5. 정확도체크
score1= ridge.score(train_scaled,train_label)
score2=ridge.score(test_scaled,test_label)
print('score1예측 : ',score1)
print('score2예측 : ',score2)

# 6. 오차범위
mae=mean_absolute_error(test_label,predict)
print('오차범위 : ', mae)
