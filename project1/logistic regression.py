# Data Wrangling
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pickle

# Visualization
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
import seaborn as sns

# Utility
import os
import sys
import time
import random
import shutil
import subprocess
import warnings; warnings.filterwarnings("ignore")
from IPython.display import Image
import IPython
from tqdm import tqdm
import platform
from itertools import combinations
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import PowerTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import StratifiedKFold,cross_val_score

train=pd.read_csv('project1/train_features.csv')
train_labels=pd.read_csv('project1/train_labels.csv')
test=pd.read_csv('project1/test_features.csv')
submission=pd.read_csv('project1/sample_submission.csv')

# # 가속도,자이로스코프,자이로-가속도값 에너지로 표현
# train['acc_xyz']  =(train['acc_x']**2+train['acc_y']**2+train['acc_z']**2)**(1/3)
# train['gy_xyz']  =(train['gy_x']**2+train['gy_y']**2+train['gy_z']**2)**(1/3)
# test['acc_xyz']  =(test['acc_x']**2+test['acc_y']**2+test['acc_z']**2)**(1/3)
# test['gy_xyz']  =(test['gy_x']**2+test['gy_y']**2+test['gy_z']**2)**(1/3)

## x,xy,xz,xyz로 확립
acc_columns = train.columns[2:5]
gy_columns = train.columns[5:]

for target_list in [acc_columns,gy_columns]:
    for a,b in combinations(target_list,2):
        column_name = a +b[-1]
        train[column_name] = (train[a]**2 + train[b]**2)**(1/2)
train['acc_xyz']  =(train['acc_x']**2+train['acc_y']**2+train['acc_z']**2)**(1/3)
train['gy_xyz']  =(train['gy_x']**2+train['gy_y']**2+train['gy_z']**2)**(1/3)

for target_list in [acc_columns,gy_columns]:
    for a,b in combinations(target_list,2):
        column_name = a +b[-1]
        test[column_name] = (test[a]**2 + test[b]**2)**(1/2)
test['acc_xyz']  =(test['acc_x']**2+test['acc_y']**2+test['acc_z']**2)**(1/3)
test['gy_xyz']  =(test['gy_x']**2+test['gy_y']**2+test['gy_z']**2)**(1/3)

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

grouped_train_x = train.iloc[:,2:].values.reshape(-1,600,train.shape[1]-2)
grouped_test_x = test.iloc[:,2:].values.reshape(-1,600,test.shape[1]-2)
print(grouped_train_x)