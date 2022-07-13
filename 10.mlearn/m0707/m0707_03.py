# 품종을 구별하는 알고리즘을 구현하시오.
# 랜덤포레스트 알고리즘 구현
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate, train_test_split
import pandas as pd
import numpy as np

# 데이터불러오기
df=pd.read_csv('10.mlearn/m0707/iris(150).csv')

data=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].to_numpy()
label=df['Species'].to_numpy()

# 데이터 전처리
train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)


# 알고리즘 선택
rf=RandomForestClassifier(random_state=42,n_jobs=-1)

# 교차 알고리즘훈련
scores=cross_validate(rf,train_data,train_label,n_jobs=-1,return_train_score=True)

print('train_score 평균: ',np.mean(scores['train_score']))
print('test_score 평균: ',np.mean(scores['test_score']))

# 정확도
rf.fit(train_data,train_label)
print('test_data score : ', rf.score(test_data,test_label))

# 특성중요도
print('중요도 :',rf.feature_importances_)