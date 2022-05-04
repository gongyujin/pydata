import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')
print(df.describe()) # 평균, 표준편차, 최소값, 최대값, 값분포도

print('키 최소값 : ', df['키'].min())
print('키 최대값 : ', df['키'].max())
print('키 평균 : ', df['키'].mean())
print('키 개수 : ', df['키'].count())
print('키 합계 : ', df['키'].sum())


print(df['키'].nlargest(3)) # 큰사람 3명을 출력해줌
print(df['키'].nsmallest(3)) # 작은사람 3명을 출력해줌

print(df)
print('학교 : ',df['학교']) # df 바로 뒤에 들어올 수 있는 것은 column만 들어올수 있음
# unique 중복제거 출력
print('학교 : ',df['학교'].unique())
# nunique 중복제거한 숫자
print('학교 : ',df['학교'].nunique())
# -------------------------------------------------------
# df=pd.read_excel('stat_142801.xls', skiprows=2,nrows=2)
# print(df)
# print(df[df.columns[-1]])
# print(df['2020'])
# print(df.columns)
# -------------------------------------------------------

# df=pd.read_excel('score.xlsx')

# # 컬럼 활용
# print(df.columns)
# print(df.columns[0])
# print(df.columns[5])
# print(df.columns[-1])
# print(df[['이름','사회','SW특기']]) # 대소문자 구별함
# print(df['SW특기'])  
# print(df[df.columns[-1]])

# -------------------------------------------------------

# # index 지정 활용
# df.set_index('이름',inplace=True) # index를 이름으로 정의함
# print(df)
# print(df.index)
# print(df.index[0])
# print(df.index[5]) # 박동현
# print(df.loc['박동현'])
# print(df.loc[df.index[5]])
# print(df.index[-1]) # 마지막 index의 이름이 출력됨
# print(df.loc[df.index[-1]]) # index의 제일마지막 row가 출력됨
# print(df.iloc[3:5])
# -------------------------------------------------------
# print(df.iloc[0])
# print(df.loc['강나래']) # index가 이름으로 정의되어서 할 수 있음
# print(df.loc[df.index[0]])

# # 1000개 출력일때 중간부분 skip됨 => df.iloc[]로 중간값을 볼수 있음
# df=pd.read_excel('user.xlsx')
# print(df)
# print(df.iloc[500:505])