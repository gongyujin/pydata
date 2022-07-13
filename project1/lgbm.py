from random import random
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lightgbm import LGBMClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold, cross_val_score, cross_validate
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm # 돌아가는 시간 보기
from glob import glob # 디렉토리 마음대로 불러오기 
## 3. Modeling
from sklearn.metrics import log_loss
import time
# "Gausain Process"라는 통계학을 기반으로 만들어진 모델로, 
# 여러개의 하이퍼 파라미터들에 대해서,
# "Aqusition Fucntion"을 적용했을 때,
# "가장 큰 값"이 나올 확률이 높은 지점을 찾아냅니다.
from bayes_opt import BayesianOptimization # grid searchm random search는 최적의 값을 찾아갈수없다는 단점있음

# 오른팔에 자이로스코프, 가속도계가 달린 센서를 착용하고 특정 운동 동작을 수행, 오른쪽 forearm에 착용
#   => '스마트워치를 착용한채 데이터 수집'과 같은 형태
# 훈련된 61개 동작중에 어떤 class에 해당하는지 맞추는 classification

# 1개 동작 수행: (0.02초 * 600frams) = 12초 , 한 frame당 0.02초
#--------------------------------------------------------------------------
# 1. 데이터 불러오기 : 3125개 데이터 (운동가지수는 3125개지만 class는 61개)
train=pd.read_csv('project1/train_features.csv')
train_labels=pd.read_csv('project1/train_labels.csv')
test=pd.read_csv('project1/test_features.csv')
submission=pd.read_csv('project1/sample_submission.csv')

# print(train['id'].value_counts()) # train: 총 600개의 timestep을 가진 시계열 센서 데이터
# print(train_labels['label_desc'].value_counts()) # label 양이 심한 불균형을 이룸
# --------------------------------------------
# 동작흐름 확인
# ex=train[train['id']==34] # Non-Exercise
# plt.plot(ex.iloc[:,1],ex.iloc[:,2])
# plt.plot(ex.iloc[:,1],ex.iloc[:,3])
# plt.plot(ex.iloc[:,1],ex.iloc[:,4])
# plt.plot(ex.iloc[:,1],ex.iloc[:,5])
# plt.plot(ex.iloc[:,1],ex.iloc[:,6])
# plt.plot(ex.iloc[:,1],ex.iloc[:,7])
# # 자이로스코프 degree/s 값을 degree로 변환해서 살펴볼것
# plt.legend(['acc_x','acc_y','acc_z','gy_x','gy_y','gy_z'])
# plt.show()

#--------------------------------------------------------------------------
# 2. 전처리과정
# augmentation 데이터 증강처리 => 과적합 줄이기 
# - orgin(가속도, dps(degree per sesond=각속도)) => 적분(속도, 각도)
# - rotation, permutation, rolling or combination augmentation 컬럼 

## feature engineering - pivot table
# dataset을 sum. mean, median, min, max, std, var으로 전처리
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

# train_data = pd.merge(X_pivot_train, train_labels.loc[:,['id','label']], on='id') # label_desc는 사용하지 않을 예정입니다.

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
        
    skf = StratifiedKFold(n_splits=3 , shuffle=True) # 교차검증 위한 선택
    main_model = LGBMClassifier(n_jobs = -1) # LGBMClassifier 모델선정
    scores = cross_val_score(main_model, scaled_train_x, train_labels.label.values, scoring='accuracy', cv=skf, n_jobs=-1)
    
    scores1=cross_validate(main_model, scaled_train_x, train_labels.label.values, cv=skf,return_train_score=True)
    print('cross_validate test_score: ',np.mean(scores1['test_score'])) 
    print('cross_validate train_score: ',np.mean(scores1['train_score']))
    
    #### 그리드서치 - 매개변수 교대로 변경, 교차검증까지 해서 score점수를 계산함.
    # n_jobs = -1 cpu코어를 모두사용, 컴퓨터가 느려짐.
    # params = {'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001),
    #     'max_depth': range(5, 20, 1),
    #     'min_samples_split': range(2, 100, 10)
    # }
    params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}
    gs = GridSearchCV(DecisionTreeClassifier(), params, n_jobs=-1)
    # 훈련
    gs.fit(scaled_train_x, train_labels.label.values)
    # 훈련후 최적의 모델을 넣어줌.
    dt = gs.best_estimator_
    print('gridsearchCV DecisionTreeClassifier score : ',dt.score(scaled_train_x, train_labels.label.values))
    
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

## modeling   
# lgbm은 메모리를 적게 차지하고 속도가 빠름, 정확도가 높음
# 단, overfitting에 민감하여 데이터의 크기가 작을 경우는 추천하지 않음, 만개이상일때 추천
lgbm_pbounds = {
    'learning_rate': (0.001,0.5), 
    'max_depth': (5,20),
    'n_estimators' : (100,300)
                }

def lgbm_opt(learning_rate,max_depth,n_estimators):
    params = {
    'learning_rate': learning_rate,
    'max_depth': int(round(max_depth)),
    'n_estimators' : int(round(max_depth))
            }
    
    lgbm = LGBMClassifier(**params)
    # Cross_val_score의 Metric이 "Neg_log_loss"이기 때문에, Negative한 값들이 나옵니다. 따라서 abs로 절대값을 씌워줍니다.
    # 이 값이 Target 값이 됩니다.
    score = 100-abs(cross_val_score(lgbm, best_train_x, train_labels.label.values, scoring='neg_log_loss', cv=4,n_jobs=-1).mean()) 
    return score
BO_lgbm = BayesianOptimization(f = lgbm_opt, pbounds = lgbm_pbounds, random_state=1) 

# 20번의 Random Search 후 20번의 최적의 Search를 합니다.
BO_lgbm.maximize(init_points=20, n_iter=20)

# Maximize를 통해 나온 Parameter가 저장되어있습니다.
max_params = BO_lgbm.max['params']
max_params['max_depth'] = int(round(max_params['max_depth'])) # Max_depth는 int값을 받기에 int로 변환합니다.
max_params['n_estimators'] = int(round(max_params['n_estimators'])) # n_estimators는 int값을 받기에 int로 변환합니다.
print(max_params)

# Model에 저장된 param을 지정해 저장후, 재 학습을 통해 predict합니다.
model_lgbm = LGBMClassifier(**max_params)
model_lgbm.fit(best_train_x,  train_labels.label.values, eval_metric = 'logloss')
prediction = model_lgbm.predict_proba(best_test_x)    
    
    