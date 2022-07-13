from sklearn.model_selection import cross_validate, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.stats import skew, kurtosis
from sklearn.manifold import TSNE

import pandas as pd
import numpy as np
import missingno
import matplotlib.pyplot as plt
import seaborn as sns
import os
from tqdm import tqdm
pd.set_option('display.max_rows', 500)

# fft는 가속도, 각속도 정보를 변환할 수 있음


train=pd.read_csv('project1/train_features.csv')
train_labels=pd.read_csv('project1/train_labels.csv')
test=pd.read_csv('project1/test_features.csv')
submission=pd.read_csv('project1/sample_submission.csv')

pd.options.display.max_columns=50

## feature engneering - augmentation
# 가속도,자이로스코프,자이로-가속도값 에너지로 표현
train['acc_t']  =(train['acc_x']**2+train['acc_y']**2+train['acc_z']**2)**(1/3)
test['acc_t']  =(test['acc_x']**2+test['acc_y']**2+test['acc_z']**2)**(1/3)

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

train_fft,test_fft = ft_trans('acc_t',train,test)
train_fft_target = train_fft.iloc[:,1:-2]

print(train_fft)
print(test_fft)
print(train_fft_target)

## 스케일링
col=train_fft.columns
train_s=train_fft.copy()
test_s=test_fft.copy()
scaler = StandardScaler()
train_s= scaler.fit_transform(train_s)
train_sc = pd.DataFrame(data = train_s,columns =col).to_numpy()
test_s= scaler.fit_transform(test_s)
test_sc = pd.DataFrame(data = test_s,columns =col).to_numpy()
# xx=np.array(train_sc).reshape(3125, 600, -1) # train_data
# test_x=np.array(test_sc).reshape(782, 600, -1) # test_data
y_label=train_labels['label'].to_numpy()
print(pd.DataFrame(data = train_s,columns =col).describe())
print(pd.DataFrame(data = test_s,columns =col).describe())

# # 알고리즘선택, 학습, 예측, 정확도
# rfc=RandomForestClassifier(n_jobs=-1, min_samples_leaf=30)
# scores=cross_validate(rfc,train_sc,y_label,n_jobs=-1,return_train_score=True)
# print('train_score 평균 : ', np.mean(scores['train_score']))
# print('test_score 평균 : ', np.mean(scores['test_score']))
# print('-'*50)

# rfc.fit(train_sc,y_label)
# print(rfc.predict_proba(test_sc))
# y_pred=rfc.predict(test_sc)
# print('randomforest 예측값 : ',y_pred)
# print('randomforest 정확도 : ',rfc.score(train_sc,y_label))

# ####### fft 반복하나로 줄이기

#list of label_id

ambiguous           =   [0,32,50]
static              =   [8,9,12,22,26,28,29,30,31,38,39,48,49,52]
Rotary_motion       =   [18,27,35,36,40,41,51,53,54,55,56,57]
vertical_motion     =   [6,10,11,13,14,16,17,23,24,33,37,42,43,44,45,46,47,60,58,59]
Rotary_vertical     =   [1,2,3,4,5,7,15,19,20,21,25,34]

cluster_label = {
    0:ambiguous,
    1:static,
    2:Rotary_motion,
    3:vertical_motion,
    4:Rotary_vertical
}

ids_cluster_dic={}
for ids,labels in train_labels[['id','label']].values:
    for key,value in cluster_label.items():
        if labels in value:
            ids_cluster_dic[ids] = key
            
label_color = ['red','red','blue','blue','blue']

# perplexity 에 따른 TSNE 군집 시각화
# 동적, 정적 운동의 구분이 어느정도 진행 되는것으로 보임, FFT를 통한 주파수 값으로 접근하는 방향이 용이 해보임
for v in range(10,50,10):
    tsns=TSNE(n_components=2, perplexity=v,random_state=42)
    tsns_trans = tsns.fit_transform(train_fft_target.values)


    plt.figure(figsize=(8,6))
    for i in range(len(train_fft_target)): 

        
        color_num = label_color[ids_cluster_dic[i]]
        if color_num =='red':
            labels = 'static'
        else:
            labels = 'dynamic'
        
        plt.scatter(tsns_trans[i][0],tsns_trans[i][1],c=color_num,s=50,alpha=0.3,label=labels)




    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(),loc='upper right')
    # plt.xlim(-20,30)
    # plt.ylim(-15,10)
    plt.xlabel("x_t-SNE",fontsize=13)
    plt.ylabel("y_t-SNE",fontsize=13)
    plt.title("t-SNE FFT data \nperplexity %d"%v,fontsize=16 )
    plt.show()
    
t_df = train_labels.groupby('label').head(2).sort_values('label').reset_index(drop=True)

def draw(ids):
    t1 =train[train.id ==ids]
    ts = t1.acc_t -t1.acc_t.mean()
    ts.index =pd.date_range('2020-01-01 00:00:00', periods=600, freq='20ms')

    fmax = 50      # sampling frequency 
    dt = 1/fmax      # sampling period
    N  = 600      # length of signal
    t  = np.arange(0,N)*dt   # time = [0, dt, ..., (N-1)*dt]
    x = ts.values

    work_out_name = t_df.loc[t_df.id ==ids]['label_desc'].values[0]



    f, axs = plt.subplots(2,1,figsize=(15,10))
    f.suptitle(work_out_name,fontsize=18)
    #     plt.title("acc_total")

    axs[0].set_title("acc_total")
    axs[0].plot(ts)
    axs[0].set_xlabel('time(sec)')


    df = fmax/N   # df = 1/N = fmax/N
    f = np.arange(0,N)*df     #   frq = [0, df, ..., (N-1)*df]
    xf = np.fft.fft(x)*dt

    axs[1].stem(f[0:int(N/2+1)],np.abs(xf[0:int(N/2+1)]))
    axs[1].set_title("FFT")
    axs[1].set_xlabel('frequency(Hz)'); plt.ylabel('abs(xf)'); plt.grid()


    plt.show()
    
draw(165)
# 스쿼트의 경우 1HZ 미만 (1HZ : 1초에 1번) 에서 높은 값을 가지는 경향을 보인다
draw(65)
# Squat Rack shoulder press (아마 seated shoulder press일듯) 의 경우
# 숄더 프레스가 전완 사용이 많기 때문에, 노이즈로 보이는 값이 많이 찍힌 것으로 보인다.
# 10~15HZ 의 (10 HZ: 1초에 10번) 전완이 부들부들(?) 한 것으로 보인 수치가 찍힘
# max feak의 경우 1HZ 미만으로 근육의 고립에 집중해서 운동을 한것으로 보인다.
draw(301)
# 딥스의 경우 체중을 전완과 삼각근 만으로 온전히 지탱해야하기 때문에
# 10~15HZ 에서 분포가 증가하는것을 보니 전완이 부들부들 했던것으로 판단된다.
draw(53)