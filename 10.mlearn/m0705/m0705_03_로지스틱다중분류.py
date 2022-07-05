from sklearn.linear_model import LogisticRegression # 로지스틱회귀 - 분류
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # 정규화, 표준화
from scipy.special import expit # 시그모이드 함수
from scipy.special import softmax # z점수 0-1 사이의 값으로 변경해줌
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터불러오기
df_fish=pd.read_csv('10.mlearn/m0704/fish.csv')
# print(df_fish.columns)

data=df_fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
label=df_fish['Species'].to_numpy() # 물고기 종류 : 7가지, ['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']

# 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 정규화, 표준화작업
ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)

# 로지스틱회귀 - 다중분류
# 알고리즘 선택
# 선형회귀 - 규제 : 릿지회귀 - alpha제어
# 대문자, 기본값 C=1 ; 낮으면 규제강함, 높으면 규제약함

# # 규제 데이터 추출 및 그래프 그리기
# c_lists=[0.001,0.01,0.1,1,10,100]
# train_score=[]
# test_score=[]
# for c_list in c_lists:
#     lr=LogisticRegression(C=c_list)

#     # 알고리즘 훈련
#     lr.fit(train_scaled,train_label)
#     # 정확도
#     train_score.append(lr.score(train_scaled,train_label))
#     test_score.append(lr.score(test_scaled,test_label))

# # 그래프 그리기
# plt.plot(np.log10(c_lists),train_score)
# plt.plot(np.log10(c_lists),test_score)
# plt.show()

# 알고리즘 선택
lr=LogisticRegression(C=10)

# 알고리즘 훈련
lr.fit(train_scaled,train_label)


# 예측
# proba=lr.predict_proba(test_scaled[:5])
print("'Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish'") # decision_function은 label의 사전순서대로 순서를 예측함
proba=lr.predict(test_scaled[:5])
print(proba)

# # 정확도
# score1=lr.score(train_scaled,train_label)
# score2=lr.score(test_scaled,test_label)
# print('정확도1 : ',score1)
# print('정확도2 : ',score2)

# z점수
decision=lr.decision_function(test_scaled[:5])
# print('z값 : ',decision)

# 시그모이드 점수 : 로지스틱 다중분류일때는 확률의 합이 1이 될 수 없음 => 소프트맥스함수를 대신 사용
# 다중분류 : 소프트맥스함수, 이진분류 : 시그모이드함수
print(np.round(softmax(decision,axis=1),3)) # 행방향으로 더했을때 softmax 확인, 3째자리까지 round

