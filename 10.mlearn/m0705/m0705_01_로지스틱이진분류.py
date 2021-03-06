from sklearn.linear_model import LogisticRegression
# from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split # 데이터 분리
from sklearn.preprocessing import StandardScaler # 정규화, 표준화
from scipy.special import expit # 시그모이드함수
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 선형회귀 - 기울기,y절편 z=ax+b => 예측값=기울기*특성값+y절편
# 로지스틱회귀 - class2개, class 여러개 지도학습(분류), 정확도가 나와야함 (%)

df_fish=pd.read_csv('10.mlearn/m0705/fish.csv')

data=df_fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
label=df_fish['Species'].to_numpy()
# print(df_fish['Species'].unique())
# ['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt'] # class 7개
# ['Weight', 'Length', 'Diagonal', 'Height', 'Width'] # 특성 5개


# # 데이터전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# Bream, Smel ;도미, 빙어
index1=(train_label =='Bream') | (train_label=='Smelt')
index2=(test_label =='Bream') | (test_label=='Smelt')
train_bream_smelt = train_data[index1] # 119개 -> 33개 데이터만 뽑아옴
train_label2=train_label[index1]
test_bream_smelt=test_data[index2] # 40개 -> 16개 데이터만 뽑아옴
test_label2=test_label[index2]
# 정규화,표준화작업
ss=StandardScaler()
train_scaled=ss.fit_transform(train_bream_smelt)

test_scaled=ss.fit_transform(test_bream_smelt)

# 알고리즘선택
lr=LogisticRegression()

# 실습훈련
lr.fit(train_scaled,train_label2)
print('-'*50)
print(lr.coef_,lr.intercept_) # 기울기 5개 : 특성 5개 z= ax1 + bx2 + cx3 + dx4 + ex5 + y절편
print('-'*50)

# 예측
result=lr.predict(test_scaled[:5])
print('결과값 : ', result)
result2=lr.predict_proba(test_scaled[:5]) 
print('결과값2 : ', result2)

# 시그모이드 함수 : 0-1사이에 있는 값으로 출력되게 함
# z값을 출력 : z= ax1 + bx2 + cx3 + dx4 + ex5 + y절편
decisions=lr.decision_function(test_scaled[:5]) # 예측값이 됨, 정규화해서 마이너스가 나옴
print(decisions)

# 시그모이드 함수 적용
# z값이 0과1이 값으로 변형됨 => proba에서 나온 결과값과 같음, 결국 proba값은 z값을 0~1값으로 퍼센트화한것
print(expit(decisions)) 
 

# # 정확도
# score1=lr.score()
# score2=lr.score()
# print('score1정확도 : ',score1)
# print('score2정확도 : ',score2)