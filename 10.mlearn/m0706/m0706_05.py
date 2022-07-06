from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from scipy.special import expit
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
# 길이 30, 무게 600 -> 도미인지, 빙어인지 분류하시오.
# decisiontreeclassifier 사용

# [ 도미 ] =1 ,35개
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0,
33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0,
610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# [ 빙어 ] =0 ,14개
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

length=bream_length+smelt_length # 49개
weight=bream_weight+smelt_weight

data=np.column_stack((length,weight))
label=np.concatenate((['도미']*35,['빙어']*14))

train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

# train_score=[]
# test_score=[]
# for idx in range(1,20):
#     dt=DecisionTreeClassifier(max_depth=idx,random_state=42)
#     dt.fit(train_data,train_label)
#     train_score.append(dt.score(train_data,train_label))
#     test_score.append(dt.score(test_data,test_label))
# plt.plot(train_score)
# plt.plot(test_score)
# plt.show()

dt=DecisionTreeClassifier(random_state=42)
# dt=KNeighborsClassifier()
dt.fit(train_data,train_label)
# print(dt.feature_importances_)
print('30,600 예측값 : ',dt.predict([[30,600]]))
print('25,150 예측값 : ',dt.predict([[25,150]]))
print('train score : ',dt.score(train_data,train_label))
print('test score : ',dt.score(test_data,test_label))

plt.figure(figsize=(10,7))
plot_tree(dt,filled=True,feature_names=['length','weight'])
plt.show()

