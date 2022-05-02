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

df.loc['합계']=[df['사고건수(건)'].sum(),df['사망자수(명)'].sum(),df['부상자수(명)'].sum(),df['교통사고 피해수(명)'].sum()]

df.loc['평균']=[df['사고건수(건)'][:-1].mean().astype(int),df['사망자수(명)'][:-1].mean().astype(int),df['부상자수(명)'][:-1].mean().astype(int),df['교통사고 피해수(명)'][:-1].mean().astype(int)]
print(df)
# print(df.info())

# df[컬럼][index]
print(df['사고건수(건)'][1])
# df.loc[index명,컬럼]
print(df.loc['02월','사고건수(건)'])