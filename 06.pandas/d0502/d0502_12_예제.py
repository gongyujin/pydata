# 사회점수평가 컬럼추가
# 90이상 A
# 80이상 B
# 70이상 C
# 60이상 D

# 컬럼순서변경 -> 사회,사회점수평가

import pandas as pd

def result(score):
    if score>=90:
        result='A'
    elif score>=80:
        result='B'
    elif score>=70:
        result='C'
    elif score>=60:
        result='D'
    else:
        result='F'
    return result        


df=pd.read_excel('score.xlsx',index_col='지원번호')
print(df)

df['사회점수평가']='F'
df['사회점수평가']=df['사회'].apply(result)

print(df)

# df.columns 컬럼명들을 list
cols=list(df.columns)

df=df[cols[0:8]+[cols[-1]]+[cols[-2]]]
print(df)

# 국어,영어,수학,과학,사회
# 합계, 평균 컬럼을 만들고 평균에 따른 평가컬럼추가
df['합계']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['평균']=df['합계']/5

df['평균점수평가']='F'
df['평균점수평가']=df['평균'].apply(result)

print(df)