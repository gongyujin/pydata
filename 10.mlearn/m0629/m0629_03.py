from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 1. 데이터 가져오기 - muschroom.csv
df=pd.read_csv('10.mlearn/m0629/mushroom.csv')
data=df[['cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment','gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']]
label=df['poisonous']

attr_list=[]
for i in range(len(data)):
    row_data=[]
    for v in range(len(data.iloc[i])):
        row_data.append(ord(data.iloc[i,v]))
    attr_list.append(row_data)    
data=attr_list

    
# data=[]
# label=[]
# attr_list=[]
# # iterrows -> 2개 리턴 (index,list)
# for row_index,rows in df.iterrows():
#     label.append(rows[0])
#     row_data=[]
#     for v in rows[1:]:
#         row_data.append(ord(v)) # 아스키코드 변환 후 저장
#     data.append(row_data)
    

# 2. 데이터 전처리
# train_data,test_data,train_label,test_label=train_test_split(data,label)
train_data,test_data,train_label,test_label=train_test_split(data,label,stratify=label)

# 3. 알고리즘 선택
clf=KNeighborsClassifier()

# 4. 실습훈련
clf.fit(train_data,train_label)

# 5. 예측
result=clf.predict(test_data)
print('result : ', result)

# 6. 정답률
score1=clf.score(train_data,train_label)
score2=clf.score(test_data,test_label)
print('train score : ', score1)
print('test score : ', score2)
