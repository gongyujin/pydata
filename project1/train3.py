###### 1. Loading Data
import pandas as pd

###### 2. EDA
import numpy as np
import matplotlib.pyplot as plt
import random

###### 3. Setting Data
from itertools import combinations
import math
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PowerTransformer, MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler, OneHotEncoder
from tqdm import tqdm

import shap
from sklearn.feature_selection import SelectKBest, SelectPercentile
from sklearn.model_selection import cross_val_score, cross_validate
from scipy.ndimage import gaussian_filter1d
from sklearn.decomposition import PCA
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.cluster import KMeans
from scipy.stats import skew, kurtosis
import os
# os.mkdir('features')


###### 4. Modeling
from sklearn.metrics import mean_squared_error, log_loss, make_scorer
from sklearn.model_selection import RandomizedSearchCV,train_test_split, StratifiedKFold, GridSearchCV

import time
from bayes_opt import BayesianOptimization
from vecstack import stacking
from datetime import datetime

###### # 5. Make Submission
from scipy.stats import gmean

###### ETC
import warnings
warnings.filterwarnings('ignore')
train_x = pd.read_csv('project1/train_features.csv')
train_y = pd.read_csv('project1/train_labels.csv')
test_x = pd.read_csv('project1/test_features.csv')
submission=pd.read_csv('project1/sample_submission.csv')

train = pd.merge(train_x,train_y,on='id')
train = train.groupby(['label','time']).agg('mean').reset_index().drop(columns = ['id'])
label_name = train_y.iloc[:,1:].sort_values(by='label').drop_duplicates().drop(columns = ['label'])
label_name.index = range(61)
label_name = label_name.to_dict()['label_desc']
target_columns = list(train.columns[2:])


# feature generation
acc_columns = train_x.columns[2:5]
gy_columns = train_x.columns[5:]

for target_list in [acc_columns,gy_columns]:
    for a,b in combinations(target_list,2):
        column_name = a +b[-1]
        train_x[column_name] = (train_x[a]**2 + train_x[b]**2)**(1/2)
train_x['acc_xyz'] = (train_x['acc_x']**2 + train_x['acc_y']**2 + train_x['acc_z']**2)**(1/3)
train_x['gy_xyz'] = (train_x['gy_x']**2 + train_x['gy_y']**2 + train_x['gy_z']**2)**(1/3)

for target_list in [acc_columns,gy_columns]:
    for a,b in combinations(target_list,2):
        column_name = a +b[-1]
        test_x[column_name] = (test_x[a]**2 + test_x[b]**2)**(1/2)
test_x['acc_xyz']  =(test_x['acc_x']**2+test_x['acc_y']**2+test_x['acc_z']**2)**(1/3)
test_x['gy_xyz']  =(test_x['gy_x']**2+test_x['gy_y']**2+test_x['gy_z']**2)**(1/3)

agg_train_x  = pd.pivot_table(data = train_x, # X_train의 데이터를 통해서
    values = train_x.columns[2:],  # id와 time을 제외한 피쳐를 대상으로
    index = 'id', # id를 기준으로 잡아
    aggfunc = ['sum','mean',         # 합, 평균
        'median','min','max', # 중앙값 최소값, 최대값
        'std','var'           # 베셀 보정 표본 표준편차, 비편향 편차 의 값을 구합니다.
    ]
).reset_index()

agg_test_x  = pd.pivot_table(data = test_x, #
    values = test_x.columns[2:], 
    index = 'id', # id를 기준으로 잡아
    aggfunc = ['sum','mean',        
        'median','min','max',
        'std','var'          
    ]
).reset_index()

columns = ['id']+[agg+'_'+name for agg,name in agg_train_x.columns][1:]
agg_train_x.columns = columns
agg_test_x.columns = columns

agg_train_x.to_csv('project1/features/agg_train.csv',index=False)
agg_test_x.to_csv('project1/features/agg_test.csv',index=False)

# 600초끼리 묶기
# Make Feature with Logloss
grouped_train_x = train_x.iloc[:,2:].values.reshape(-1,600,train_x.shape[1]-2)
grouped_test_x = test_x.iloc[:,2:].values.reshape(-1,600,test_x.shape[1]-2)
# n sec change Data
for num in ['002','010','020','030','050','100','200','300','600']:
    target_time = float(num[0]+'.'+num[1:])
    globals()['log_'+num+'_train_x'] = np.zeros((grouped_train_x.shape[0],grouped_train_x.shape[1]-int(target_time//0.02), grouped_train_x.shape[2]))
    globals()['log_'+num+'_test_x'] = np.zeros((grouped_test_x.shape[0],grouped_test_x.shape[1]-int(target_time//0.02), grouped_test_x.shape[2]))

def time_log_data(data, data_name, num, user_id, t):
    target_time = float(num[0]+'.'+num[1:])
    try:
        globals()['log_'+num+'_'+data_name][user_id][t] = data[user_id][t + int(target_time // 0.02)] - data[user_id][t]
    except:
        pass
    

for data,data_name in zip([grouped_train_x, grouped_test_x],['train_x','test_x']):
    for user_id in tqdm(range(data.shape[0])):
        for t in range(599):
            for num in ['002','010','020','030','050','100','200','300','600']:
                time_log_data(data, data_name, num, user_id, t)
print('== Making Log Data Done ==')
columns = ['id'] + list(train_x.columns[2:])

for data_name in ['train_x','test_x']:
    for num in ['002','010','020','030','050','100','200','300','600']:
        log_num = globals()['log_'+num+'_'+data_name].shape[1]
        globals()['log_'+num+'_'+data_name] = pd.DataFrame(globals()['log_'+num+'_'+data_name].reshape(-1,14)).reset_index()
        globals()['log_'+num+'_'+data_name].columns = columns
        globals()['log_'+num+'_'+data_name].id = globals()['log_'+num+'_'+data_name].id.apply(lambda x: x//log_num)
print('==Log Data to DF done==')

for num in tqdm(['002','010','020','030','050','100','200','300','600']):
    globals()['log_'+num+'_train_x'] = pd.pivot_table(globals()['log_'+num+'_train_x'], values = globals()['log_'+num+'_train_x'].columns[1:], index='id', 
        aggfunc = ['sum','mean',        
        'median','min','max',
        'std','var'        
    ]
                            ).reset_index()

    globals()['log_'+num+'_test_x'] = pd.pivot_table(globals()['log_'+num+'_test_x'], values = globals()['log_'+num+'_test_x'].columns[1:], index='id', 
        aggfunc = ['sum','mean',        
        'median','min','max',
        'std','var'        
    ]
                           ).reset_index()
    columns = ['id'] + ['log_change_'+num+'_'+agg+'_'+name for agg,name in globals()['log_'+num+'_train_x'].columns][1:]
    globals()['log_'+num+'_train_x'].columns =  columns
    globals()['log_'+num+'_test_x'].columns = columns
log_change_train = pd.DataFrame(list(range(3125)), columns = ['id'])
log_change_test = pd.DataFrame(list(range(3125,3907 )), columns = ['id'])
for num in ['002','010','020','030','050','100','200','300','600']:
    log_change_train = pd.merge(log_change_train, globals()['log_'+num+'_train_x'])
    globals()['log_'+num+'_test_x'].id = globals()['log_'+num+'_test_x'].id + 3125
    log_change_test = pd.merge(log_change_test, globals()['log_'+num+'_test_x'])
print('==Log CHANGE DF to Pivot Table Done==')

log_change_train.to_csv('project1/features/log_change_train.csv',index=False)
log_change_test.to_csv('project1/features/log_change_test.csv',index=False)

# n sec skip
columns = ['id'] + list(train_x.columns[2:])
for num in tqdm(['002','010','020','030','050','100','200','300','600']):
    target_time = float(num[0]+'.'+num[1:])
    skip_num = int(num)//2
    target_index = list(range(0,600,skip_num)) + [599]
    globals()['log_'+num+'_train_x'] = pd.DataFrame(grouped_train_x[:,target_index,:].reshape(-1,14)).reset_index()
    globals()['log_'+num+'_train_x'].columns = columns
    globals()['log_'+num+'_train_x'].id = globals()['log_'+num+'_train_x'].id.apply(lambda x : x//len(target_index))
    globals()['log_'+num+'_test_x'] = pd.DataFrame(grouped_test_x[:,target_index,:].reshape(-1,14)).reset_index()
    globals()['log_'+num+'_test_x'].columns = columns
    globals()['log_'+num+'_test_x'].id = globals()['log_'+num+'_test_x'].id.apply(lambda x : x//len(target_index))

for num in tqdm(['002','010','020','030','050','100','200','300','600']):
    globals()['log_'+num+'_train_x'] = pd.pivot_table(globals()['log_'+num+'_train_x'], values = globals()['log_'+num+'_train_x'].columns[1:], index='id', 
        aggfunc = ['sum','mean',         # 합, 평균
        'median','min','max', # 중앙값 최소값, 최대값
        'std','var'           # 베셀 보정 표본 표준편차, 비편향 편차 의 값을 구합니다.
    ]
                            ).reset_index()

    globals()['log_'+num+'_test_x'] = pd.pivot_table(globals()['log_'+num+'_test_x'], values = globals()['log_'+num+'_test_x'].columns[1:], index='id', 
        aggfunc = ['sum','mean',         # 합, 평균
        'median','min','max', # 중앙값 최소값, 최대값
        'std','var'           # 베셀 보정 표본 표준편차, 비편향 편차 의 값을 구합니다.
    ]
                           ).reset_index()
    columns = ['id'] + ['log_skip_'+num+'_'+agg+'_'+name for agg,name in globals()['log_'+num+'_train_x'].columns][1:]
    globals()['log_'+num+'_train_x'].columns =  columns
    globals()['log_'+num+'_test_x'].columns = columns

log_skip_train = pd.DataFrame(list(range(3125)), columns = ['id'])
log_skip_test = pd.DataFrame(list(range(3125,3907 )), columns = ['id'])
for num in ['002','010','020','030','050','100','200','300','600']:
    log_skip_train = pd.merge(log_skip_train, globals()['log_'+num+'_train_x'])
    globals()['log_'+num+'_test_x'].id = globals()['log_'+num+'_test_x'].id + 3125
    log_skip_test = pd.merge(log_skip_test, globals()['log_'+num+'_test_x'])
print('==Log SKIP DF to Pivot Table Done==')

log_skip_train.to_csv('project1/features/log_skip_train.csv',index=False)
log_skip_test.to_csv('project1/features/log_skip_test.csv',index=False)

smoothed_train_x = pd.DataFrame()
smoothed_test_x = pd.DataFrame()

for user_id in tqdm(range(train_x['id'].nunique())):
    temp = train_x.query('id == @user_id')
    temp.iloc[:,2:] = gaussian_filter1d(temp.iloc[:,2:], axis= 0, sigma=10)
    smoothed_train_x = pd.concat([smoothed_train_x, temp])


for user_id in tqdm(range(test_x['id'].nunique())):
    temp = test_x.query('id == @user_id')
    temp.iloc[:,2:] = gaussian_filter1d(temp.iloc[:,2:], axis= 0, sigma=10)
    smoothed_test_x = pd.concat([smoothed_test_x, temp])


smoothed_agg_train_x = pd.pivot_table(train_x, values = train_x.columns[2:], index='id', 
                         aggfunc=['sum','mean',         # 합, 평균
        'median','min','max', # 중앙값 최소값, 최대값
        'std','var'           # 베셀 보정 표본 표준편차, 비편향 편차 의 값을 구합니다.
    ]
                        ).reset_index()
print('==TRAIN DATA DONE ==')
smoothed_agg_test_x = pd.pivot_table(test_x, values = test_x.columns[2:], index='id', 
                        aggfunc=['sum','mean',         # 합, 평균
        'median','min','max', # 중앙값 최소값, 최대값
        'std','var'           # 베셀 보정 표본 표준편차, 비편향 편차 의 값을 구합니다.
    ]
                       ).reset_index()
print('==TEST DATA DONE ==')
columns = ['id']+['smoothed'+'_'+agg+'_'+name for agg,name in smoothed_agg_train_x.columns][1:]
smoothed_agg_train_x.columns = columns
smoothed_agg_test_x.columns = columns

smoothed_agg_train_x.to_csv('project1/features/smoothed_agg_train.csv',index=False)
smoothed_agg_test_x.to_csv('project1/features/smoothed_agg_test.csv',index=False)

### fft
def ft_trans(name,train,test):
    
    def train_test(check,num_col):

        
        if check =='train':
            df_checking=train.copy()
            train_datas = np.zeros((len(df_checking.id.unique()),304))
            
        elif check =='test':
            df_checking=test.copy()
            train_datas = np.zeros((len(df_checking.id.unique()),304))
                       

        for i,num in enumerate(tqdm(df_checking.id.unique())):

            tt = df_checking.loc[df_checking.id==num][name] -df_checking.loc[df_checking.id==num][name].mean()
            fmax = 50      # sampling frequency 1000 Hz
            dt = 1/fmax      # sampling period
            N  = 600      # length of signal

            t  = np.arange(0,N)*dt   # time = [0, dt, ..., (N-1)*dt]
            x = tt.values
            df = fmax/N   # df = 1/N = fmax/N
            f = np.arange(0,N)*df     #   frq = [0, df, ..., (N-1)*df]
            xf = np.fft.fft(x)*dt
            tq_index=f[0:int(N/2+1)]
            tq_abs= np.abs(xf[0:int(N/2+1)])

            results = pd.DataFrame(tq_abs,tq_index).reset_index().rename(columns={'index':'hz',0:'abs_value'})
            
            ar0 = np.array([num])
            ar1 =results.abs_value.values
            ar2 = np.array([skew(results.abs_value),kurtosis(results.abs_value, fisher=True)])
            return_value = np.concatenate([ar0,ar1 ,ar2])    
            train_datas[i] = return_value

        return train_datas

    
    col_ft = ['_'+str(x) for x in range(304)]
    
    num_col = len(col_ft)
    train_datas = train_test('train',num_col)
    test_datas = train_test('test',num_col)
    
    col_ft_F = ['id']+[name+"_"+x for x in col_ft[1:]]        
    train_df = pd.DataFrame(train_datas,columns= col_ft_F)
    test_df = pd.DataFrame(test_datas,columns= col_ft_F)
    
    train_df.id = train_df.id.astype('int')
    test_df.id = test_df.id.astype('int')
    
    
    return train_df ,test_df

train_fft,test_fft = ft_trans('acc_xyz',train_x,test_x)
train_fft.to_csv('project1/features/fft_train.csv',index=False)
test_fft.to_csv('project1/features/fft_test.csv',index=False)

agg_train_x = pd.read_csv('project1/features/agg_train.csv')
agg_test_x = pd.read_csv('project1/features/agg_test.csv')

log_change_train = pd.read_csv('project1/features/log_change_train.csv')
log_change_test = pd.read_csv('project1/features/log_change_test.csv')

log_skip_train = pd.read_csv('project1/features/log_skip_train.csv')
log_skip_test = pd.read_csv('project1/features/log_skip_test.csv')

smoothed_agg_train = pd.read_csv('project1/features/smoothed_agg_train.csv')
smoothed_agg_test = pd.read_csv('project1/features/smoothed_agg_test.csv')


fft_train = pd.read_csv('project1/features/fft_train.csv')
fft_test = pd.read_csv('project1/features/fft_test.csv')

total_train_x = pd.concat([agg_train_x, log_change_train, log_skip_train,smoothed_agg_train, fft_train], axis= 1).drop(columns = ['id'])
total_test_x = pd.concat([agg_test_x, log_change_test, log_skip_test,smoothed_agg_test, fft_test], axis= 1).drop(columns = ['id'])


# 최종
total_train_x.to_csv('project1/features/concated_train_x.csv',index=False)
total_test_x.to_csv('project1/features/concated_test_x.csv',index=False)

# class KMeansFeaturizer:
#     """Transforms numeric data into k-means cluster memberships.
    
#     This transformer runs k-means on the input data and converts each data point
#     into the id of the closest cluster. If a target variable is present, it is 
#     scaled and included as input to k-means in order to derive clusters that
#     obey the classification boundary as well as group similar points together.

#     Parameters
#     ----------
#     k: integer, optional, default 100
#         The number of clusters to group data into.

#     target_scale: float, [0, infty], optional, default 5.0
#         The scaling factor for the target variable. Set this to zero to ignore
#         the target. For classification problems, larger `target_scale` values 
#         will produce clusters that better respect the class boundary.

#     random_state : integer or numpy.RandomState, optional
#         This is passed to k-means as the generator used to initialize the 
#         kmeans centers. If an integer is given, it fixes the seed. Defaults to 
#         the global numpy random number generator.

#     Attributes
#     ----------
#     cluster_centers_ : array, [k, n_features]
#         Coordinates of cluster centers. n_features does count the target column.
#     """

#     def __init__(self, k=100, target_scale=5, random_state=None):
#         self.k = k
#         self.target_scale = target_scale
#         self.random_state = random_state
#         self.cluster_encoder = OneHotEncoder().fit(np.array(range(k)).reshape(-1,1))
        
#     def fit(self, X, y=None):
#         """Runs k-means on the input data and find centroids.

#         If no target is given (`y` is None) then run vanilla k-means on input
#         `X`. 

#         If target `y` is given, then include the target (weighted by 
#         `target_scale`) as an extra dimension for k-means clustering. In this 
#         case, run k-means twice, first with the target, then an extra iteration
#         without.

#         After fitting, the attribute `cluster_centers_` are set to the k-means
#         centroids in the input space represented by `X`.

#         Parameters
#         ----------
#         X : array-like or sparse matrix, shape=(n_data_points, n_features)

#         y : vector of length n_data_points, optional, default None
#             If provided, will be weighted with `target_scale` and included in 
#             k-means clustering as hint.
#         """
#         if y is None:
#             # No target variable, just do plain k-means
#             km_model = KMeans(n_clusters=self.k, n_init=20, random_state=self.random_state)
#             km_model.fit(X)

#             self.km_model_ = km_model
#             self.cluster_centers_ = km_model.cluster_centers_
#             return self

#         # There is target information. Apply appropriate scaling and include
#         # into input data to k-means            
#         data_with_target = np.hstack((X, y[:,np.newaxis]*self.target_scale))

#         # Build a pre-training k-means model on data and target
#         km_model_pretrain = KMeans(n_clusters=self.k, n_init=20, random_state=self.random_state)
#         km_model_pretrain.fit(data_with_target)

#         # Run k-means a second time to get the clusters in the original space
#         # without target info. Initialize using centroids found in pre-training.
#         # Go through a single iteration of cluster assignment and centroid 
#         # recomputation.
#         km_model = KMeans(n_clusters=self.k, 
#                           init=km_model_pretrain.cluster_centers_[:,:data_with_target.shape[1]-1], 
#                           n_init=1, max_iter=1)
#         km_model.fit(X)
        
#         self.km_model = km_model
#         self.cluster_centers_ = km_model.cluster_centers_
#         return self
        
#     def transform(self, X, y=None):
#         """Outputs the closest cluster id for each input data point.

#         Parameters
#         ----------
#         X : array-like or sparse matrix, shape=(n_data_points, n_features)

#         y : vector of length n_data_points, optional, default None
#             Target vector is ignored even if provided.

#         Returns
#         -------
#         cluster_ids : array, shape[n_data_points,1]
#         """
#         clusters = self.km_model.predict(X)
#         onehot = self.cluster_encoder.transform(clusters.reshape(-1,1)).toarray()
#         max_col = onehot.shape[1]
#         pca = PCA(n_components=max_col, random_state=0).fit(onehot)
#         cumsum = np.cumsum(pca.explained_variance_ratio_)
#         num_col = np.argmax(cumsum >= 0.99) + 1
#         if num_col == 1: num_col = max_col
#         pca = PCA(n_components = num_col, random_state=0).fit_transform(onehot)
#         return pd.DataFrame(pca)
    
#     def fit_transform(self, X, y=None):
#         """Runs fit followed by transform.
#         """
#         self.fit(X, y)
#         return self.transform(X, y)

total_train_x = pd.read_csv('project1/features/concated_train_x.csv')
total_test_x = pd.read_csv('project1/features/concated_test_x.csv')
    
# kmf_hint = KMeansFeaturizer(k=5, target_scale=5, random_state=0).fit(total_train_x, train_y.label.values)
# training_cluster_features = kmf_hint.transform(total_train_x)
# test_cluster_features = kmf_hint.transform(total_test_x)

# total_train_x = pd.concat([total_train_x, training_cluster_features],axis=1)
# total_test_x = pd.concat([total_test_x, test_cluster_features],axis=1)

# total_train_x.to_csv('project1/features/final_train_x.csv',index=False)
# total_test_x.to_csv('project1/features/final_test_x.csv',index=False)

#############################################################
## 스케일링
def find_best_scaler(train_x, test_x, train_y):
    best_score = 100
    columns = 'scaled_'+train_x.columns
    for scaler in [PowerTransformer(), MinMaxScaler(), StandardScaler(), MaxAbsScaler(), RobustScaler()]:        
        scaled_train_x = scaler.fit_transform(train_x)
        scaled_train_x = pd.DataFrame(scaled_train_x, columns = columns).astype('float64')
        scaled_test_x = scaler.transform(test_x)
        scaled_test_x = pd.DataFrame(scaled_test_x, columns = columns).astype('float64')
        skf = StratifiedKFold(n_splits=3 , shuffle=True)
        rf = RandomForestClassifier()
        scores = [abs(x) for x in cross_val_score(rf, scaled_train_x, train_y.label.values, scoring='neg_log_loss', cv=skf, n_jobs=-1)]
        print(scaler.__class__.__name__)
        print(f'TOTAL 최대성능: {min(scores)}\n평균성능: {np.mean(scores)}')
        print('-'*30)
        
        if np.mean(scores) < best_score:
            best_score = np.mean(scores)
            best_train_x = scaled_train_x
            best_test_x = scaled_test_x
            best_scaler = scaler
    
    print('BEST SCALER : ', best_scaler.__class__.__name__)
    
    return best_score, best_train_x, best_test_x, best_scaler


_, scaled_train_x, scaled_test_x, scaler = find_best_scaler(total_train_x,total_test_x, train_y)



final_train_x=scaled_train_x
final_test_x=scaled_test_x
# final_train_x = pd.concat([total_train_x, scaled_train_x],axis=1)
# final_test_x = pd.concat([total_test_x, scaled_test_x],axis=1)

final_train_x.columns = range(1, final_train_x.shape[1]+1)
final_test_x.columns = range(1, final_test_x.shape[1]+1)
print(final_train_x)
print(final_train_x.shape)


### modeling   
import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense, LSTM
fianl_train=tf.reshape(np.array(final_train_x),[-1,1,2263]) #4526
X=fianl_train
final_test=tf.reshape(np.array(final_test_x),[-1,1,2263])
y = tf.keras.utils.to_categorical(train_y['label']) 
# model = Sequential()
# model.add(LSTM(32, input_shape=(1,2263)))
# model.add(Dense(128, activation='relu'))
# model.add(Dense(61, activation='softmax'))

# model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# model.fit(fianl_train,y, epochs=30, batch_size=128, validation_split=0.2)
# prediction=model.predict(final_test)
# submission.iloc[:,1:]=prediction
# submission.to_csv('project1/features/sample_submission7.csv', index=False)


#### 알고리즘선택, 학습, 예측, 정확도
# final_train = final_train_x.to_numpy()
# final_test = final_test_x.to_numpy()

# rfc=RandomForestClassifier(n_jobs=-1, random_state=0, min_samples_leaf=30)
# scores=cross_validate(rfc,final_train,train_y.label.values,n_jobs=-1,return_train_score=True)
# print('train_score 평균 : ', np.mean(scores['train_score']))
# print('test_score 평균 : ', np.mean(scores['test_score']))
# print('-'*50)

# rfc.fit(final_train,train_y.label.values)
# rfc_proba=rfc.predict_proba(final_test)
# y_pred=rfc.predict(final_test)
# print('randomforest 예측값 : ',y_pred)
# print('randomforest 정확도 : ',rfc.score(final_train,train_y.label.values))
# index=[i for i in range(0,61)]
# df_rfc_proba=pd.DataFrame(rfc_proba,columns=index)
# submission.iloc[:,1:]=df_rfc_proba
# submission.to_csv('project1/features/sample_submission6.csv',index=False)

# ###### 데이타 변환
# pwf = PowerTransformer(standardize=True).fit(final_train_x)
# X_train = pwf.transform(final_train_x)

# # 사용할 모델 설정 (속도가 빠른 모델 사용 권장)
# fs_model = LogisticRegression(random_state=0, n_jobs=-1) 

# # 각 특성과 타깃(class) 사이에 유의한 통계적 관계가 있는지 계산하여 특성을 선택하는 방법 
# cv_scores = []
# for p in tqdm(range(130, min(X_train.shape[1], 200), 1)):
#     X_new = SelectKBest(k=p).fit_transform(X_train, train_y.label.values)    
#     kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)
#     cv_score = cross_val_score(fs_model, X_new, train_y.label.values, scoring='neg_log_loss', cv=kfold, n_jobs=-1)
#     cv_scores.append((p, cv_score.mean(), cv_score.max()))

# # Print the best percentile
# best_score = cv_scores[np.argmax([score for _, score, _ in cv_scores])]  # 평균score가 제일 높을 때
# print(best_score)
# best_score = cv_scores[np.argmax([score for _, _, score in cv_scores])]  # 최대score가 제일 높을 때
# print(best_score)

# # Plot the performance change with p
# plt.plot([k for k, _, _ in cv_scores], [score for _, score, _ in cv_scores])
# plt.xlabel('Percent of features')
# plt.grid()
# plt.show()


# from keras.models import Sequential
# from keras.layers import Dense, LSTM,Bidirectional,Dropout
# from keras.layers import Dense
# from keras.layers import Dropout
# from keras.layers import LSTM
# from keras.layers.convolutional import Conv1D
# from keras.layers.convolutional import MaxPooling1D
# from keras.utils import to_categorical
# from keras import backend as K 
# from keras.callbacks import EarlyStopping, ModelCheckpoint,ReduceLROnPlateau
# from sklearn.model_selection import KFold,StratifiedKFold
# from numpy.random import seed
# import keras

# def cnn_model(input_shape, classes):
#     seed(2021)
#     tf.random.set_seed(2021)
    
#     input_layer = keras.layers.Input(input_shape)
#     conv1 = keras.layers.Conv1D(filters=128, kernel_size=9, padding='same')(input_layer)
#     conv1 = keras.layers.BatchNormalization()(conv1)
#     conv1 = keras.layers.Activation(activation='relu')(conv1)
#     conv1 = keras.layers.Dropout(rate=0.3)(conv1)

#     conv2 = keras.layers.Conv1D(filters=256, kernel_size=6, padding='same')(conv1)
#     conv2 = keras.layers.BatchNormalization()(conv2)
#     conv2 = keras.layers.Activation('relu')(conv2)
#     conv2 = keras.layers.Dropout(rate=0.4)(conv2)
    
#     conv3 = keras.layers.Conv1D(128, kernel_size=3,padding='same')(conv2)
#     conv3 = keras.layers.BatchNormalization()(conv3)
#     conv3 = keras.layers.Activation('relu')(conv3)
#     conv3 = keras.layers.Dropout(rate=0.5)(conv3)
    
#     gap = keras.layers.GlobalAveragePooling1D()(conv3)
    
#     output_layer = keras.layers.Dense(classes, activation='softmax')(gap)
    
#     model = keras.models.Model(inputs=input_layer, outputs=output_layer)
    
#     model.compile(loss='categorical_crossentropy', optimizer = keras.optimizers.Adam(), 
#         metrics=['accuracy'])
    
#     return model

# skf = StratifiedKFold(n_splits = 10, random_state = 2021, shuffle = True)
# reLR = ReduceLROnPlateau(patience = 4,verbose = 1,factor = 0.5) 
# es =EarlyStopping(monitor='val_loss', patience=8, mode='min')

# accuracy = []
# losss=[]
# models=[]
# for i, (train, validation) in enumerate(skf.split(X, y.argmax(1))) :
#     mc = ModelCheckpoint(f'./model_kf/cv_study{i + 1}.h5',save_best_only=True, verbose=0, monitor = 'val_loss', mode = 'min', save_weights_only=True)
#     print("-" * 20 +"Fold_"+str(i+1)+ "-" * 20)
#     model = cnn_model((600,18),61)
#     history = model.fit(X[train], y[train], epochs = 100, validation_data= (X[validation], y[validation]), 
#                         verbose=1,batch_size=64,callbacks=[es,mc,reLR])
#     model.load_weights(f'./model_kf/cv_study{i + 1}.h5')
    
#     k_accuracy = '%.4f' % (model.evaluate(X[validation], y[validation])[1])
#     k_loss = '%.4f' % (model.evaluate(X[validation], y[validation])[0])
    
#     accuracy.append(k_accuracy)
#     losss.append(k_loss)
#     models.append(model)

# print('\nK-fold cross validation Auc: {}'.format(accuracy))
# print('\nK-fold cross validation loss: {}'.format(losss))

# print(sum([float(i) for i in accuracy])/10)
# print()
# print(sum([float(i) for i in losss])/10)

# preds = []
# for model in models:
#     pred = model.predict(final_test)
#     preds.append(pred)
# pred = np.mean(preds, axis=0)
# pred
# submission=pd.read_csv('project1/features/sample_submission8.csv')
