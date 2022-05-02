import pandas as pd

df=pd.read_excel('인구통계2.xls',index_col='행정구역')
print(df)

# 총인구수 컬럼추가
# 도시 컬럼 추가
# 총인구수 >= 5000000 : 대도시
# 총인구수 < 500000 : 소도시
# 그외는 중도시
print(df.columns)
df['총인구수']=df['2021년_남자 인구수']+df['2021년_여자 인구수']
df['도시']='중도시'

filt=df['총인구수']>=5000000
df.loc[filt,'도시']='대도시'
filt=df['총인구수']<2000000
df.loc[filt,'도시']='소도시'
print(df)
print(df.index)

# 합계 row를 추가
# 2021_세대수, 남자인구수,여자인구수, 총인구수 ,도시는 0
df.loc['합계']=[df['2021년_세대수'].sum(),df['2021년_남자 인구수'].sum(),\
    df['2021년_여자 인구수'].sum(),df['총인구수'].sum(),0]
print(df)