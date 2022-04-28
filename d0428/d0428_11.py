from turtle import pd
import pandas as pd
# 컬럼의 선택
df=pd.read_excel('score.xlsx',index_col='지원번호')
# 컬럼의 모두 출력
print(df.columns)
print(df.columns[0]) # 컬럼만 출력하기 위한 명령어

# 컬럼의 내용을 출력
print(df['이름']) # 컬럼 전체를 출력하는 명령어
print(df[['학교','국어']]) # 컬럼2개 내용을 출력할때 [[]]대괄호 2개
print(df[df.columns[-1]]) # 마지막 컬럼 전체를 출력

# print(df.columns[[1,3,-1]]) # 컬럼 title 3개를 출력할때 [[]] 대괄호 2개
print(df[df.columns[[1,3,-1]]])

print(df['영어'])
print(df[['이름','영어']][0:5]) # 영어 컬럼의 내용 row 5개 출력 (컬럼에 대한 슬라이싱)
print(df[0:5]) # row를 찍으려면 iloc를 사용해야하지만 column에서 사용하려면 그냥 슬라이싱하면 됨
print(df[:3]) # 0부터 3이전까지 출력
print(df[4:]) # 4부터 끝까지 출력

# print(df[1]) # 단순하게 index번호를 넣으면 안찍힘 ==> error

print(df.iloc[0:5]) # 한개만 출력할때는 row만 출력 => iloc, loc 사용