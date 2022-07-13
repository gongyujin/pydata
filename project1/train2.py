from random import random
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
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
import scipy
from transforms3d.axangles import axangle2mat
from math import atan, sqrt
from scipy.integrate import cumtrapz
# 오른팔에 자이로스코프, 가속도계가 달린 센서를 착용하고 특정 운동 동작을 수행, 오른쪽 forearm에 착용
#   => '스마트워치를 착용한채 데이터 수집'과 같은 형태
# 훈련된 61개 동작중에 어떤 class에 해당하는지 맞추는 classification

# 1개 동작 수행: (0.02초 * 600frams) = 12초 , 한 frame당 0.02초
#--------------------------------------------------------------------------
# 1. 데이터 불러오기 : 3125개 데이터 (운동가지수는 3125개지만 class는 61개)
train=pd.read_csv('project1/train_features.csv')
train_acc, train_gy  = train.iloc[:, 2:5], train.iloc[:, 5:]
train_time = train.time[:600]/50
train_labels=pd.read_csv('project1/train_labels.csv')
test=pd.read_csv('project1/test_features.csv')
submission=pd.read_csv('project1/sample_submission.csv')
y_label=train_labels['label'].to_numpy()
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

def rolling(data):
    for j in np.random.choice(data.shape[0], int(data.shape[0]*2/3)):
        data[j] = np.roll(data[j], np.random.choice(data.shape[1]), axis= 0)
    return data

def rotation(data):
    axis = np.random.uniform(low=-1, high=1, size=data.shape[1])
    angle = np.random.uniform(low=-np.pi, high=np.pi)
    return np.matmul(data , axangle2mat(axis,angle))

def permutation(data, nPerm=4, mSL=10):
    data_new = np.zeros(data.shape)
    idx = np.random.permutation(nPerm)
    bWhile = True
    while bWhile == True:
        segs = np.zeros(nPerm+1, dtype=int)
        segs[1:-1] = np.sort(np.random.randint(mSL, data.shape[0]-mSL, nPerm-1))
        segs[-1] = data.shape[0]
        if np.min(segs[1:]-segs[0:-1]) > mSL:
            bWhile = False
    pp = 0
    for ii in range(nPerm):
        data_temp = data[segs[idx[ii]]:segs[idx[ii]+1],:]
        data_new[pp:pp+len(data_temp),:] = data_temp
        pp += len(data_temp)
    return(data_new)

def combine_aug(data, k, aug_P = 0):
    data_ = data.copy()
    if aug_P == 0:
        if (k+1) % 2 == 0:
            for i in np.random.choice(int(data.shape[0]/600), int(data.shape[0]/600*2/3)):
                data_[600*i:600*(i+1)] = rotation(np.array(data_[600*i:600*(i+1)]))
        if (k+1) % 2 == 1:
            for i in np.random.choice(int(data.shape[0]/600), int(data.shape[0]/600*2/3)):
                data_[600*i:600*(i+1)] = permutation(np.array(data_[600*i:600*(i+1)]))
                
    if aug_P != 0:
        pass
    return data_


def get_mag(data):
    return (data.iloc[:, 0]**2) + (data.iloc[:, 1]**2) + (data.iloc[:, 2]**2)

def get_mul(data):
    return data.iloc[:, 0] * data.iloc[:, 1] * data.iloc[:, 2]


##########################################################################################################################

def get_roll_pitch(data):
    roll = (data.iloc[:,1]/(data.iloc[:,0]**2 + data.iloc[:,2]**2).apply(lambda x : sqrt(x))).apply(lambda x : atan(x))*180/np.pi
    pitch = (data.iloc[:,0]/(data.iloc[:,1]**2 + data.iloc[:,2]**2).apply(lambda x : sqrt(x))).apply(lambda x : atan(x))*180/np.pi
    return pd.concat([roll, pitch], axis= 1)

##########################################################################################################################

def setting(data, data_, case = 0):
    if case == 0:
        for i in range(0, data.shape[0], 600):
            data[i] = data_[i] - data_[i+599]
    else:
        for i in range(0, data.shape[0], 600):
            data[i: i+5] = data_[i: i+5].values - data_[i+594:i+599].values
    return data
        
def get_diff(data, case = 0):
    if case == 0:
        x_dif, y_dif, z_dif = data.iloc[:, 0].diff(), data.iloc[:, 1].diff(), data.iloc[:, 2].diff()
    else:
        x_dif, y_dif, z_dif = data.iloc[:, 0].diff(5), data.iloc[:, 1].diff(5), data.iloc[:, 2].diff(5)
    return pd.concat([setting(x_dif, data.iloc[:, 0], case),
                      setting(y_dif, data.iloc[:, 1], case),
                      setting(z_dif, data.iloc[:, 2], case)], axis= 1)
############################################################################################################################

def get_cumtrapz(acc):
    acc_x, acc_y, acc_z = [], [], []
    ds_x, ds_y, ds_z = [], [], []
    for i in range(int(acc.shape[0]/600)):
        acc_x.append(pd.DataFrame(cumtrapz(acc.iloc[600*i:600*(i+1), 0], train_time, initial=0)))
        acc_y.append(pd.DataFrame(cumtrapz(acc.iloc[600*i:600*(i+1), 1], train_time, initial=0)))
        acc_z.append(pd.DataFrame(cumtrapz(acc.iloc[600*i:600*(i+1), 2], train_time, initial=0)))
        ds_x.append(pd.DataFrame(cumtrapz(cumtrapz(acc.iloc[600*i:600*(i+1), 0], train_time, initial=0), train_time, initial=0)))
        ds_y.append(pd.DataFrame(cumtrapz(cumtrapz(acc.iloc[600*i:600*(i+1), 1], train_time, initial=0), train_time, initial=0)))
        ds_z.append(pd.DataFrame(cumtrapz(cumtrapz(acc.iloc[600*i:600*(i+1), 2], train_time, initial=0), train_time, initial=0)))
    return (pd.concat([pd.concat(acc_x), pd.concat(acc_y), pd.concat(acc_z)], axis = 1).reset_index(drop=True),
           pd.concat([pd.concat(ds_x), pd.concat(ds_y), pd.concat(ds_z)], axis= 1).reset_index(drop = True))
    
def train_dataset(acc_data, gy_data, i, aug_P = 0):
    
    aug_acc = combine_aug(acc_data, i, aug_P)
    aug_gy = combine_aug(gy_data, i, aug_P)
    
    diff_acc = get_diff(aug_acc)
    #diff_acc_5 = get_diff(aug_acc, 1)
    
    roll_pitch_acc = get_roll_pitch(aug_acc)
    mag_acc, mul_acc = get_mag(aug_acc), get_mul(aug_acc)
    mag_mul_acc = pd.concat([mag_acc, mul_acc], axis= 1)
    #accvel, disp = get_cumtrapz(aug_acc)

    diff_gy = get_diff(aug_gy)
    #diff_gy_5 = get_diff(aug_gy, 1)
    mag_gy, mul_gy = get_mag(aug_gy), get_mul(aug_gy)
    mag_mul_gy = pd.concat([mag_gy, mul_gy], axis= 1)

    return pd.concat([aug_acc, diff_acc, roll_pitch_acc, mag_mul_acc,
                     aug_gy, diff_gy, mag_mul_gy], axis= 1)

def test_dataset(acc_data, gy_data):
    
    diff_acc = get_diff(acc_data)
    #diff_acc_5 = get_diff(acc_data, 1)
    
    roll_pitch_acc = get_roll_pitch(acc_data)
    mag_acc, mul_acc = get_mag(acc_data), get_mul(acc_data)
    mag_mul_acc = pd.concat([mag_acc, mul_acc], axis= 1)
    #accvel, disp = get_cumtrapz(acc_data)

    diff_gy = get_diff(gy_data)
    #diff_gy_5 = get_diff(gy_data, 1)
    mag_gy, mul_gy = get_mag(gy_data), get_mul(gy_data)
    mag_mul_gy = pd.concat([mag_gy, mul_gy], axis= 1)

    return pd.concat([acc_data, diff_acc, roll_pitch_acc, mag_mul_acc,
                      gy_data, diff_gy, mag_mul_gy], axis= 1)
    
data_for_scaler = test_dataset(train_acc, train_gy) # train data만 사용
scaler = StandardScaler().fit(np.array(data_for_scaler))

data_for_scaler = np.array(data_for_scaler).reshape(-1, 600, data_for_scaler.shape[1])
########################################################################################
test_x = test_dataset(test.iloc[:, 2:5], test.iloc[:, 5:])

test_X = scaler.transform(np.array(test_x)).reshape(-1, 600, test_x.shape[1])

print(data_for_scaler)
print(test_X)
    
# 알고리즘선택, 학습, 예측, 정확도
# params = {'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001),
#     'max_depth': range(5, 20, 1),
#     'min_samples_split': range(2, 100, 10)
# }
params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}
gs = GridSearchCV(DecisionTreeClassifier(), params, n_jobs=-1)
print('-'*50)
gs.fit(data_for_scaler,y_label)

gs_proba=gs.predict_proba(test_X)
y_pred=gs.predict(test_X)
print('gridsearchCV DecisionTreeClassifier 예측값 : ',y_pred)
print('gridsearchCV DecisionTreeClassifier 평균 정확도 : ',np.max(gs.cv_results_['mean_test_score']))   
print('gridsearchCV DecisionTreeClassifier train 정확도 : ',gs.score(data_for_scaler,y_label))   
index=[i for i in range(0,61)]
df_gs_proba=pd.DataFrame(gs_proba,columns=index)
# id=train_labels['id']
# df_gs=pd.concat([id,df_gs_proba],axis=1)
# df_gs.to_csv('sample_submission1.csv')
submission.iloc[:,1:]=df_gs_proba
submission.to_csv('sample_submission1.csv',index=False)

# 알고리즘선택, 학습, 예측, 정확도
rfc=RandomForestClassifier(n_jobs=-1, random_state=0, min_samples_leaf=30)
scores=cross_validate(rfc,data_for_scaler,y_label,n_jobs=-1,return_train_score=True)
print('train_score 평균 : ', np.mean(scores['train_score']))
print('test_score 평균 : ', np.mean(scores['test_score']))
print('-'*50)

rfc.fit(data_for_scaler,y_label)
rfc_proba=rfc.predict_proba(test_X)
y_pred=rfc.predict(test_X)
print('randomforest 예측값 : ',y_pred)
print('randomforest 정확도 : ',rfc.score(data_for_scaler,y_label))
index=[i for i in range(0,61)]
df_rfc_proba=pd.DataFrame(rfc_proba,columns=index)
submission.iloc[:,1:]=df_rfc_proba
submission.to_csv('sample_submission2.csv',index=False)


    
# ------------------------------------------------------------------------

# smoothing

