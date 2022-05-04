import pandas as pd
import numpy as np

df=pd.read_excel('score.xlsx',index_col='지원번호')

# df.dropna(axis='index',inplace=True)
# # nan이 있는 행(index) 삭제 //위에랑 같은 의미
# df.dropna()

# # axis='columns' 해당되는 열 삭제
# df.dropna(axis='columns',inplace=True)

df['학교']=np.nan

# # how='any' nan이 1개라도 있으면 column삭제
# df.dropna(axis='columns',how='any',inplace=True) # 학교, SW특기 컬럼 삭제됨

# how='all' nan이 모두있어야 column삭제
df.dropna(axis='columns',how='all',inplace=True) # 학교 컬럼만 삭제

print(df)




# # nan 데이터 처리
# df.fillna('없음',inplace=True)

# # nan 데이터 삭제
# df.dropna(inplace=True)
