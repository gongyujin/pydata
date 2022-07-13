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


import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM
X=tf.reshape(np.array(train.iloc[:,2:]),[-1, 600, 6])
y = tf.keras.utils.to_categorical(train_labels['label']) 

#가벼운 모델 생성
model = Sequential()
model.add(LSTM(32, input_shape=(600,6)))
model.add(Dense(128, activation='relu'))
model.add(Dense(61, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X,y, epochs=30, batch_size=128, validation_split=0.2)
test_X=tf.reshape(np.array(test.iloc[:,2:]),[-1, 600, 6])
prediction=model.predict(test_X)
submission.iloc[:,1:]=prediction
submission.to_csv('project1/features/baseline_submission.csv', index=False)