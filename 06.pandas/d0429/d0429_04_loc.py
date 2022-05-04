# google_movie 4,5번 --> 제목, 가격 출력하시오.

import pandas as pd


df=pd.read_excel('google_movie.xlsx',index_col=0)
df.index.name='번호'
print(df)
print(df.index)
print(df.columns)


print(df[4:6])
print(df.loc[[4,5],['제목','가격']])


print('-'*50)
print(df.loc[[4,5],'가격'])
print('-'*50)
df.loc[[4,5],'가격']=1000
print(df.loc[[4,5],'가격'])
print('-'*50)



print(df.info())