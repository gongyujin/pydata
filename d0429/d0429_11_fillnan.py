import pandas as pd
import numpy as np

df=pd.read_excel('score.xlsx',index_col='지원번호')

# nan 데이터 처리
# 결측치 : Nan 데이터 처리

# # fillna: Nan데이터를 처리할때 사용
# print(df.fillna('',inplace=True)) # 빈공백으로 채움
# print(df.fillna('없음',inplace=True)) # 없음으로 채움
# ==> fillna: 모든 nan을 처리

# print(df['SW특기'].str.contains('없음',case=False))
# filt=df['SW특기'].str.contains('없음',case=False)
# print(df[filt]) # nan이 나오면 error발생


df['학교']=np.nan # nan을 만들어줌
# df['수학']=np.nan
# 모든 nan값을 대체
# df.fillna('없음',inplace=True)
# df['학교']='없음'

# 학교 컬럼만 nan을 대체하고 싶음
# df['학교'].fillna('없음',inplace=True)

# df['수학'].fillna(0,inplace=True)
# print(df.info()) 
# # np.nan으로 바꿔버리면 먼저 float로 정의됨 
# # 대신 '없음'으로 바꾸면 object이 됨

# nan 데이터 삭제
# ------------------------------------------------
# dropna-> 해당되는 행이 삭제 (nan이 포함되면 모든 행을 삭제)
df.dropna(inplace=True)


print(df)






