from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# # 1. 데이터 전처리 (120개-train 데이터, 30개-test데이터)
# # train 데이터, test 데이터를 특정한 데이터에 치우치지 않도록 분리해야함 , 그렇지 않으면 정확도가 낮게 나옴
# # 데이터를 섞어서 분리를 하도록 하시오.
# # 150개 random 섞어서 120개-train_data, 30개-test_data 분리를 하시오.

# numpy 형태로 변형
# index 150개 배열을 만들어서
# np.random.shuffle(index)
df=pd.read_csv('10.mlearn/m0628/iris(150).csv')


data=df[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
label=df['Species']

# 데이터 전처리 : 80%, 20%으로 랜덤으로 데이터를 분리해줌
# test_size: test 데이터를 30%으로 분리해줌
# stratify=~~ : ~~을 기준으로 면밀하게 분리해줌; 데이터가 한쪽으로 쏠려서 분배되지 않게 해줌
# random_state=42 : 테이터를 랜덤으로 섞을때 균등하게 섞음
train_data,test_data,train_label,test_label=\
    train_test_split(data,label,test_size=0.3,stratify=label,random_state=42)
print(train_data)
##-------------------------------------------
# df=df[['SepalLength','SepalWidth','PetalLength','PetalWidth','Species']]
# df_numpy=df.to_numpy()
# np.random.shuffle(df_numpy) # index 150개 배열을 랜덤으로 섞어줌
# print(df_numpy)


# train_data=df_numpy[:120,:4] #(120,4)
# train_label=df_numpy[:120,4:5] #(120,1)
# test_data=df_numpy[120:,:4] #(120,4)
# test_label=df_numpy[120:,4:5] #(120,1)
## ----------------------------------------------------
# data=df[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
# label=df['Species']

# data_numpy=np.array(data)
# label_numpy=np.array(label)

# # 0~149까지의 랜덤 index만들기
# index=np.arange(150) # 150개 배열생성
# np.random.shuffle(index)
# # index를 활용해서 120개, 30개 데이터 분리
# train_data=data_numpy[index[:120]]
# train_label=label_numpy[index[:120]]
# test_data=data_numpy[index[120:]]
# test_label=label_numpy[index[120:]]

## -------------------------------------------
# train_data=df[['SepalLength','SepalWidth','PetalLength','PetalWidth']][0:120]
# # print(train_data.shape)
# train_label=df['Species'][0:120]

# test_data=df[['SepalLength','SepalWidth','PetalLength','PetalWidth']][120:]
# test_label=df['Species'][120:]
# ___________________________________________
# 2. 알고리즘선택
clf=svm.SVC()

# 3. 데이터 학습훈련 - 학습훈련데이터
clf.fit(train_data,train_label)

# 4. 데이터 예측
example=[[5.7,2.9,3.6,1]]
result=clf.predict(example)
print("결과값 : ", result)

# 5. 정답률 - test 데이터 들어감
score=clf.score(test_data,test_label)
print("정답률 : ", score)