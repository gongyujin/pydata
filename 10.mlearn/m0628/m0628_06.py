from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler # 정규화작업을 해주는 함수

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
# matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

# [ 도미 ] =1 ,35개
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0,
33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0,
610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# [ 빙어 ] =0 ,14개
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# result=['도미','도미',....,'빙어','빙어',...]
# 도미length  + 빙어length = train_data, test_data
# 도미weight + 빙어weight = train_label, test_label

length= bream_length+smelt_length
weight= bream_weight+smelt_weight

# # 1개의 list 합치기
# data=[[l,w] for l,w in zip(length,weight)]
# # print(data)

# label=['도미']*35 + ['빙어']*14

# numpy 2개의 컬럼을 묶음
data=np.column_stack((length,weight))
# ones,zeros array를 1개의 array로 변형
label=np.concatenate((np.ones(35),np.zeros(14))) # 도미:1 빙어:0

# ------------------------------------------------
# # 정규화 작업
# # (현재데이터 - 평균)/표준편차 = 표준점수
# # 평균
# mean=np.mean(data,axis=0) # 산술평균
# std=np.std(data,axis=0) # 표준편차

# # 표준점수
# train_scaled=(data-mean)/std

# # 25,150 정규화작업
# new=([25,150]-mean)/std
# ------------------------------------------------

# 1) train데이터, test 데이터 분리
train_data,test_data,train_label,test_label=train_test_split(data,label)

# 정규화작업2
ss=StandardScaler()
ss.fit(train_data) 
train_scaled=ss.transform(train_data) # (data-산술평균)/표준편차
test_scaled=ss.transform(test_data) # (data-산술평균)/표준편차
new=ss.transform([[25,150]])
# ------------------------------------------------
# 산점도 그래프
# s : 원크기설정, c : color, cmap : colormap을 사용
plt.scatter(train_scaled[:,0],train_scaled[:,1])
# train데이터 (길이, 무게)
# plt.scatter(train_data[indexs,0],train_data[indexs,1],marker="D")
plt.scatter(new[0][0],new[0][1],marker="x")
plt.show()

# ------------------------------------------------
# 알고리즘 선택
clf=KNeighborsClassifier()
# clf=svm.SVC()
# clf=MLPClassifier()

# 데이터 학습
clf.fit(train_scaled,train_label)
# # clf에 있는 train_data의 knn이웃하는 5개의 데이터를 추출
# distances, indexs = clf.kneighbors([new])
# print(indexs)
print('-'*50)

# 데이터 예측 (길이 30,무게 600의 고기를 예측)
result=clf.predict(new)
print("결과값 : ",result)
# 정답률
score=clf.score(test_scaled,test_label)
print("정답률 : ", score)

