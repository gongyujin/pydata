import pandas as pd
df=pd.read_excel('user.xlsx',index_col='id')
print(df)
print(df.columns)
print(df.index)

# 500~600, 605 row출력
# first_name, email만 출력

# 조건을 사용해서 iloc 검색 500~600, 605 출력
# loc 검색
# d1=df.loc[(df.index>=500) & (df.index<=600) | (df.index==605),['first_name','email']] 
# iloc 검색
# d1=df.iloc[(df.index>=500) & (df.index<=600) | (df.index==605),[0,2]] 
d1=df.iloc[(df.index>=500) & (df.index<=600) | (df.index==605)][['first_name','email']] 
print(d1)

