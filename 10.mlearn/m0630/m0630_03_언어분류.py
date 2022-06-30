from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import glob,os.path,re

# train,test 폴더를 일어오기위해 함수생성
def makeData(url):
    # 디렉토리 내 모든 파일 읽어오기
    files=glob.glob(url)

    data=[] #26개 a-z
    label=[] # 4개 en,fr,id,tl
    for file_name in files:     # 파일 20개
        # 위치를 제외한 파일이름
        basename=os.path.basename(file_name)
        lang=basename.split('-')[0] # 라벨
        
        # 파일읽어오기
        with open(file_name,'r',encoding='utf-8') as f:
            text=f.read() # 파일의 글을 추출
            text=text.lower()
        
            # 알파벳을 분류 
            # a,b,c,d,.....
            # [0,0,0,0,0,.....] # 26개 만들어줄거임 (알파벳은 26개니깐)
            code_a = ord('a') # 97
            code_z = ord('z') # 122
            count=[0]*26
            
            # text의 글을 1글자씩 분리
            for ch in text:
                code_current = ord(ch)
                if code_a <= code_current <= code_z: # 97 <= x <= 122
                    count[code_current-code_a]+=1
            
            # 데이터전처리, 정규화
            total=sum(count) # 전체글자수
            count=list(map(lambda n:n/total,count))
            data.append(count)
            label.append(lang)
    
    return data,label

# ----------------------------------------------------------------   
# 1. 데이터 전처리
url1='10.mlearn/m0630/train/*.txt'
url2='10.mlearn/m0630/test/*.txt'
train_data,train_label=makeData(url1)
test_data,test_label=makeData(url2)

url3='10.mlearn/m0630/fr-100.txt'
url4='10.mlearn/m0630/en-100.txt'
test_data1,test_label1=makeData(url3)
test_data2,test_label2=makeData(url4)

# 2. 알고리즘선택
# clf=KNeighborsClassifier(n_neighbors=3)
clf=svm.SVC()

# 3. 학습
clf.fit(train_data,train_label)

# 4. 예측
result=clf.predict(test_data)
print('결과값 : ', result)
result2=clf.predict(test_data1)
print('결과값 : ', result2)
result3=clf.predict(test_data2)
print('결과값 : ', result3)

# 5. 정답률
score1=clf.score(train_data,train_label)
score2=clf.score(test_data,test_label)
score3=clf.score(test_data1,test_label1)
score4=clf.score(test_data2,test_label2)
print('train 정답률 : ', score1)
print('test 정답률 : ', score2)
print('test1 정답률 : ', score3)
print('test2 정답률 : ', score4)