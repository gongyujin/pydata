# 4개의 입력을 만들어서
# 입력된 데이터를 가지고, 해당품종을 분류하는 프로그램을
# 구축하시오.

from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df=pd.read_csv('10.mlearn/m0628/iris(150).csv')
print(df.describe())

data=df[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
label=df['Species']

# 데이터 전처리 : 80%, 20%으로 랜덤으로 데이터를 분리해줌
# test_size: test 데이터를 30%으로 분리해줌
# stratify=~~ : ~~을 기준으로 면밀하게 분리해줌; 데이터가 한쪽으로 쏠려서 분배되지 않게 해줌
# random_state=42 : 테이터를 랜덤으로 섞을때 균등하게 섞음
train_data,test_data,train_label,test_label=\
    train_test_split(data,label,test_size=0.3,stratify=label,random_state=42)

SepalLength=input('SepalLength 길이를 입력하세요. (4.3-7.9)>> ')
SepalWidth=input('SepalWidth 길이를 입력하세요. (2.0-4.4)>> ')
PetalLength=input('PetalLength 길이를 입력하세요. (1.0-6.9)>> ')
PetalWidth=input('PetalWidth 길이를 입력하세요. (0.1-2.5)>> ')

example=[[SepalLength,SepalWidth,PetalLength,PetalWidth]]

clf=svm.SVC()
clf.fit(train_data,train_label)
result=clf.predict(example)
print(result)

score=clf.score(test_data,test_label)
print(score)