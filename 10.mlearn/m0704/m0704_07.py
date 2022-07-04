from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

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


clf=KNeighborsClassifier()
clf.fit(train_scaled,train_label)

new_scaled=ss.fit_transform([[105,15.2,19.5,5.09,3.42]])
result=clf.predict(test_scaled[:5])
print('예측결과 : ',result)

# proba=clf.predict_proba(new_scaled)
proba=clf.predict_proba(test_scaled[:5])
print('전체예측결과 : ',np.round(proba,decimals=4)) #  7개의 label중 확률계산

score1=clf.score(test_scaled,test_label)
print('test 정답률 : ',score1)
score2=clf.score(train_scaled,train_label)
print('train 정답률 : ',score2)