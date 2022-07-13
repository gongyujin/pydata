import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, cross_validate
from sklearn.preprocessing import MinMaxScaler, StandardScaler
# randomforest baseline을 이용
# -------------------------------------------------------------------------
# 오른팔에 자이로스코프, 가속도계가 달린 센서를 착용하고 특정 운동 동작을 수행, 오른쪽 forearm에 착용
#   => '스마트워치를 착용한채 데이터 수집'과 같은 형태
# 훈련된 61개 동작중에 어떤 class에 해당하는지 맞추는 classification

# 1개 동작 수행: (0.02초 * 600frams) = 12초 , 한 frame당 0.02초
#--------------------------------------------------------------------------
# 1. 데이터 불러오기 : 3125개 데이터
# shape : ((1875000, 8), (3125, 3), (469200, 8), (782, 62)) 
train=pd.read_csv('project1/train_features.csv')
train_labels=pd.read_csv('project1/train_labels.csv')
test=pd.read_csv('project1/test_features.csv')
submission=pd.read_csv('project1/sample_submission.csv')
y_label=train_labels['label']

# print(train['id'].value_counts()) # train: 총 600개의 timestep을 가진 시계열 센서 데이터
# print(train_labels['label_desc'].value_counts()) # label 양이 심한 불균형을 이룸
# --------------------------------------------
# #### 동작흐름 확인
# ex=train[train['id']==34] # Non-Exercise
# plt.plot(ex.iloc[:,2:])
# plt.legend(['acc_x','acc_y','acc_z','gy_x','gy_y','gy_z'])
# plt.show()

#--------------------------------------------------------------------------
# 2. 전처리과정
# augmentation 데이터 증강처리 => 과적합 줄이기 
# - orgin(가속도, dps(degree per sesond=각속도)) => 적분(속도, 각도)
# - rotation, permutation, rolling or combination augmentation 컬럼 
# smoothing

# # dataset을 max,min,mean으로 전처리, randomforest 알고리즘 사용
# features=['id','acc_x','acc_y','acc_z','gy_x','gy_y','gy_z']
# x_train=train[features].groupby('id').agg(['max','min','mean']) # 같은 운동동작간의 max, min, mean값 구해줌
# x_test=test[features].groupby('id').agg(['max','min','mean']) 


X_pivot_train = pd.pivot_table(data = train, # X_train의 데이터를 통해서
    values = train.columns[2:],  # id와 time을 제외한 피쳐를 대상으로
    index = 'id', # id를 기준으로 잡아
    aggfunc = ['sum','mean',         # 합, 평균
        'median','min','max', # 중앙값 최소값, 최대값
        'std','var'           # 베셀 보정 표본 표준편차, 비편향 편차 의 값을 구합니다.
    ]
)

X_pivot_test = pd.pivot_table(data = test, #
    values = test.columns[2:], 
    index = 'id', # id를 기준으로 잡아
    aggfunc = ['sum','mean',        
        'median','min','max',
        'std','var'          
    ]
)

X_columns = [agg + '_' + column for agg,column in X_pivot_train.columns]
X_pivot_train.columns = X_columns
X_pivot_test.columns = X_columns
X_pivot_train = X_pivot_train.reset_index()
X_pivot_test = X_pivot_test.reset_index()

## scaling - 스케일링하지않은것, minmaxscaler, standarscaler 세가지중 score가 가장높은 것으로 선정
best_score = 0
columns = 'scaled_' + X_pivot_train.columns
for scaler in [None, MinMaxScaler(), StandardScaler()]: # scaling하는 방식 3가지
    if scaler == None:
        scaled_train_x = X_pivot_train.copy()
        scaled_test_x = X_pivot_test.copy()
    else:
        scaled_train_x = scaler.fit_transform(X_pivot_train)
        scaled_train_x = pd.DataFrame(scaled_train_x, columns = columns).astype('float64')
        scaled_test_x = scaler.transform(X_pivot_test)
        scaled_test_x = pd.DataFrame(scaled_test_x, columns = columns).astype('float64')
        

    rfc=RandomForestClassifier(n_jobs=-1, random_state=0, min_samples_leaf=30)
    skf = StratifiedKFold(n_splits=3 , shuffle=True) # 교차검증 위한 선택
    scores = cross_val_score(rfc, scaled_train_x, train_labels.label.values, scoring='accuracy', cv=skf, n_jobs=-1)
    
    scores1=cross_validate(rfc,X_pivot_train,y_label,n_jobs=-1,return_train_score=True)
    print('train_score 평균 : ', np.mean(scores1['train_score']))
    print('test_score 평균 : ', np.mean(scores1['test_score']))
    print('-'*50)
    
    if scaler == None : print('NON_SCALED')
    else:    
        print(scaler.__class__.__name__)
    print(f'TOTAL 최대성능: {max(scores)}\n평균성능: {np.mean(scores)}')
    print('-'*30)

    if np.mean(scores) >= best_score:
        best_score = np.mean(scores)
        best_train_x = scaled_train_x
        best_test_x = scaled_test_x
        best_scaler = scaler

if best_scaler == None:
    print('BEST SCALER IS NON_SCALED')
else:
    print('BEST SCALER : ', best_scaler.__class__.__name__)
## best_train_data는 best scaler를 통해 스케일링된 데이터를 의미함

# train_data = pd.merge(X_pivot_train, train_labels.loc[:,['id','label']], on='id') # label_desc는 사용하지 않을 예정입니다.
# train_data.label = train_data.label.astype('category')
# ----------------------------------------
# 알고리즘선택, 학습, 예측, 정확도
rfc=RandomForestClassifier(n_jobs=-1, random_state=0, min_samples_leaf=30)
scores=cross_validate(rfc,best_train_x,y_label,n_jobs=-1,return_train_score=True)
print('train_score 평균 : ', np.mean(scores['train_score']))
print('test_score 평균 : ', np.mean(scores['test_score']))
print('-'*50)

rfc.fit(best_train_x,y_label)
print(rfc.predict_proba(best_test_x))
y_pred=rfc.predict(best_test_x)
print('randomforest 예측값 : ',y_pred)
print('randomforest 정확도 : ',rfc.score(best_train_x,y_label))