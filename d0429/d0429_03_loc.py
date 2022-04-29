import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')

# # 컬럼명을 가지고 출력
# print(df[['이름','학교']][0:5])
# print(df)
# print(df['국어'][0])


# rows기준으로 출력
print(df.loc[['1번','2번']])
# DataFrame 슬라이싱
print(df[0:2]) #df바로 뒤에 컬럼밖에 못들어오는데 row를 보고 싶을때는 loc를 붙이거나 슬라이싱으로 뽑을 수 있음

# rows 1번학생의 column 국어성적 출력
print(df.loc['1번','국어'])

# 1번,2번 국어점수 출력
print(df.loc[['1번','2번'],'국어'])
# 1번,3번 국어,영어 점수 출력
print(df.loc[['1번','3번'],['국어','영어']])

# 슬라이싱 사용 [] 1개만 사용
print(df.loc['1번':'5번','국어':'사회'])




