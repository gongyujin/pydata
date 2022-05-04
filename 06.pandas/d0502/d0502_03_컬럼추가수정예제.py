import pandas as pd

# df=pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)

# 상단 2개는 삭제
# 컬럼추가
# 사고건수, 사망자수, 부상자수, 교통사고 피해수 (사망자수+부상자수)
df=pd.read_excel('2020년월별교통사고01.xlsx',skiprows=2,index_col='월')
print(df.index) # index출력
print(df.columns) # 컬럼출력

df['교통사고 피해수(명)']=df['사망자수(명)']+df['부상자수(명)']
print(df)

df.loc['합계']=[0,0,0,0]
df.loc['합계','사고건수(건)']=df['사고건수(건)'].sum()
df.loc['합계','사망자수(명)']=df['사망자수(명)'].sum()
df.loc['합계','부상자수(명)']=df['부상자수(명)'].sum()
df.loc['합계','교통사고 피해수(명)']=df['교통사고 피해수(명)'].sum()
df.loc['평균']=[0,0,0,0]
df.loc['평균','사고건수(건)']=df['사고건수(건)'][:12].mean().astype(int)
df.loc['평균','사망자수(명)']=df['사망자수(명)'][:12].mean().astype(int)
df.loc['평균','부상자수(명)']=df['부상자수(명)'][:12].mean().astype(int)
df.loc['평균','교통사고 피해수(명)']=df['교통사고 피해수(명)'][:12].mean().astype(int)
print(df)
# print(df.info())



## 1. 사고건수가 평균보다 낮은 row의 값은 삭제하시오.
# filt=df['사고건수(건)']< df.loc['평균','사고건수(건)']
# df.drop(index=df[filt].index,inplace=True)

## 평균사고건수보다 낮은 것을 제외하고 row 출력
# filt=df['사고건수(건)']> df['사고건수(건)'][:12].mean().astype(int)
# print(df[filt].index)
# print(df[df['사고건수(건)']> df.loc['평균','사고건수(건)']])
print(df)

# 2. 사망자수가 230미만은 row삭제
# filt=df['사망자수(명)']<230
# print(df[filt].index)
# df.drop(index=df[filt].index,inplace=True)
# print(df)



# print(df['사고건수(건)'][1])
# print(df.loc['02월','사고건수(건)'])