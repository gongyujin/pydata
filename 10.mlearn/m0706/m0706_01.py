from sklearn.linear_model import SGDClassifier # 확률적경사하강법
from sklearn.model_selection import train_test_split # train, test
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
fish_df = pd.read_csv('10.mlearn/m0705/fish.csv')
# print(fish_df.columns)

data=fish_df[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
label=fish_df['Species'].to_numpy()
# print(label.unique()) # 7개 class
# print(data.info()) # 5개 특성
# print(data.describe())

# 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# 데이터 정규화, 표준화작업
ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)

# SGD : 분류
# fit : 리셋후 다시 fit함
# partial_fit : fit을 업데이트 하는 것
# sc=SGDClassifier(loss='log_loss',random_state=42)
# train_score=[]
# test_score=[]
# classes=np.unique(train_label) # 7개
# for idx in range(300):
#     sc.partial_fit(train_scaled,train_label,classes=classes) # 분류해야할 것이 총 몇개인지 파악해야함
#     train_score.append(sc.score(train_scaled,train_label))
#     test_score.append(sc.score(test_scaled,test_label))
    
# plt.plot(range(300),train_score)
# plt.plot(range(300),test_score)
# plt.xlabel('epoch')
# plt.ylabel('accuracy')
# plt.show()


######## (분류) log_loss : 로지스틱 손실함수
# sc=SGDClassifier(loss='log_loss',max_iter=100,tol=None,random_state=42)
# sc.fit(train_scaled,train_label)
# print('score train : ',sc.score(train_scaled,train_label))
# print('score test : ',sc.score(test_scaled,test_label))


####### (분류) hinge: svm 알고리즘손실함수
sc=SGDClassifier(loss='hinge',max_iter=100,tol=None,random_state=42)
sc.fit(train_scaled,train_label)
print('score train : ',sc.score(train_scaled,train_label))
print('score test : ',sc.score(test_scaled,test_label))


