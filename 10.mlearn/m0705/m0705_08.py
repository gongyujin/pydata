from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터 불러오기
df=pd.read_csv('10.mlearn/m0705/iris(150).csv')
data=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].to_numpy()
label=df['Species'].to_numpy()


train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

ss=StandardScaler()
train_scaled=ss.fit_transform(train_data)
test_scaled=ss.fit_transform(test_data)

# --------------------------
# classes=np.unique(train_label)

# sc=SGDClassifier(loss='log_loss',random_state=42)
# train_score=[]
# test_score=[]
# for i in range(300):
#     sc.partial_fit(train_scaled,train_label,classes=classes)
#     train_score.append(sc.score(train_scaled,train_label))
#     test_score.append(sc.score(test_scaled,test_label))
    
# plt.plot(range(300),train_score)
# plt.plot(range(300),test_score)
# plt.xlabel('epoch')
# plt.ylabel('accuracy')
# plt.show()

sc=SGDClassifier(loss='log_loss',max_iter=100,tol=None,random_state=42)
sc.fit(train_scaled,train_label)
sc.partial_fit(train_scaled,train_label)

score1=sc.score(train_scaled,train_label)
score2=sc.score(test_scaled,test_label)
print('train 정확도 : ',score1)
print('test 정확도 : ',score2)

# tol의 값: 반복학습을 진행함, tol 지정값보다 큰 경우에만 반복
# tol=1e-5 ; max_iter에 도달하지 않더라도 작업 중단 ==> tol보다 작게 나타나면 작업중단