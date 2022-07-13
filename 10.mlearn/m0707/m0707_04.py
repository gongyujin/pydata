import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate, train_test_split

df=pd.read_csv('10.mlearn/m0707/mushroom.csv')
print(df.columns)

data=df[['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor','gill-attachment', 'gill-spacing', 'gill-size', 'gill-color','stalk-shape', 'stalk-root', 'stalk-surface-above-ring','stalk-surface-below-ring', 'stalk-color-above-ring','stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number','ring-type', 'spore-print-color', 'population', 'habitat']]
label=df['poisonous']

list=[]
for i in range(len(data)):
    tr_row=[]
    for i2 in range(len(data.iloc[i])):
        tr_row.append(ord(data.iloc[i,i2]))
    list.append(tr_row)
    
data=list

train_data,test_data,train_label,test_label=train_test_split(data,label,random_state=42)

rf=RandomForestClassifier(random_state=42,n_jobs=-1)

scores=cross_validate(rf,train_data,train_label,n_jobs=-1,return_train_score=True)

print('train_score 평균 : ', np.mean(scores['train_score']))
print('test_score 평균 : ', np.mean(scores['test_score']))

rf.fit(train_data,train_label)

print(rf.predict_proba(test_data))
print('test 결과값 : ',rf.predict(test_data))
print('test_data score : ', rf.score(test_data,test_label))