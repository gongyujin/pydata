from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# 데이터불러오기
df_fish=pd.read_csv('10.mlearn/m0704/fish.csv')
# print(df_fish.columns)

data=df_fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
label=df_fish['Species'].to_numpy() # 물고기 종류 : 7가지, ['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']
print(df_fish['Species'].unique())

# 무개 : 105,길이 : 15.2, 대각선 : 19.5, 높이 : 5.09, 두께: 3.42
# 물고기인지 분류하시오.
# knn을 사용하기

train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)

######## 2진분류
# Bream, Smelt만 남겨놓고 나머지는 삭제
# [[False,True,False,True....]]
bream_smelt_index1=(train_label=='Bream') | (train_label == 'Smelt') 
bream_smelt_index2=(test_label=='Bream') | (test_label == 'Smelt') 
# print(bream_smelt_index) # numpy는 true,false로 분류할수있음
train_bream_smelt=train_scaled[bream_smelt_index1]
train_label=train_label[bream_smelt_index1]
test_bream_smelt=test_scaled[bream_smelt_index2]
test_label=test_label[bream_smelt_index2]
print(train_bream_smelt.shape)
print(test_bream_smelt.shape)
# train_bream_smelt, test_bream_smelt,train_label, test_label


# 알고리즘 선택
# clf=KNeighborsClassifier()
lr=LogisticRegression() # 선형회귀 lr.coef_ : 기울기, lr.intercept_ : y절편
lr.fit(train_bream_smelt,train_label)

# proba=clf.predict_proba(new_scaled)
proba=lr.predict_proba(test_bream_smelt[:5])
print('전체예측결과 : ',np.round(proba,decimals=4)) #  7개의 label중 확률계산

score1=lr.score(test_bream_smelt,test_label)
print('test 정답률 : ',score1)
score2=lr.score(train_bream_smelt,train_label)
print('train 정답률 : ',score2)