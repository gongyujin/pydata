import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# 데이터 불러오기
df=pd.read_csv('10.mlearn/m0707/picher_stats_2017.csv')
data=df[['팀명', '승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9','볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR','연봉(2017)']]
label=df['연봉(2018)']

# 데이터 전처리 - 팀 순위
team_names=df['팀명'].unique()
# 1. sk, 2. 두산, 3.한화,4.기아, 5.삼성, 6. 롯데, 7. lg, 8.kt, 9.nc
team_num=[1,7,4,6,8,2,5,3,9]

# '승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9','볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR','팀명 가중치'
##### 팀명별 가중치 설정
data_list=[]
for i in range(len(data)):
    per_data=[]
    for v in range(1,len(data.iloc[i])):
        per_data.append(data.iloc[i,v])
    for idx, name in enumerate(team_names):
        if data.iloc[i,0]==name:
            per_data.append(team_num[idx])
            break
    data_list.append(per_data)
data=data_list

train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)    

#####################################################
# lr=LinearRegression()

# lr.fit(train_data,train_label)
# print('train score : ', lr.score(train_data,train_label))
# print('test score : ', lr.score(test_data,test_label))
# # df['예측 연봉(2018)']=lr.predict(data)
# # print(df)


# ######## 원핫인코딩 컬럼추가#########################
# one_encording = pd.get_dummies(df['팀명'])
# df=df.join(one_encording)
# data=df[['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9','볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR', '연봉(2017)', 'KIA', 'KT', 'LG', 'NC', 'SK', '두산', '롯데', '삼성','한화']]
# label=df['연봉(2018)']
# train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)    

# lr=LinearRegression()

# lr.fit(train_data,train_label)
# print('train score : ', lr.score(train_data,train_label))
# print('test score : ', lr.score(test_data,test_label))
# df['예측 연봉(2018)']=lr.predict(data)
# print(df)

#####################################################
rf=RandomForestRegressor(random_state=42,n_jobs=-1)

scores=cross_validate(rf,train_data,train_label,n_jobs=-1,return_train_score=True)

print('train_score 평균 : ', np.mean(scores['train_score']))
print('test_score 평균 : ', np.mean(scores['test_score']))

rf.fit(train_data,train_label)
print('test_data score : ', rf.score(test_data,test_label))
df['예측 연봉(2018)']=rf.predict(data)
print(df)