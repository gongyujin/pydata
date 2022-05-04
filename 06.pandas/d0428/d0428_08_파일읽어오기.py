from operator import index
import pandas as pd

# # csv파일 읽어오기, index_col 지원번호를 index로 지정
# # skiprows는 1번째줄을 삭제후 가져옴
# df=pd.read_csv('score.csv',skiprows=1)
# print(df)

# csv파일 읽어오기, index_col 지원번호를 index로 지정

# skiprows 지정해서 지울수 있음
# skiprows [0,1,3,5] ==> -0,1,3,5번째줄은 제외하고 가져오기
# skiprows는 1번째줄을 삭제후 가져옴 , nrows는 n개만큼 가져오라는 의미 - 1번째줄은 컬럼으로 인식
df=pd.read_excel('stat_142801.xls',skiprows=[0,1,3,5], nrows=2,index_col=0)
print(df)
print(df.index)
print(df['2020']) # 컬럼 출력
# print(df.loc['출생아 수']) # row 
# 출력


# print(df)

# # txt파일 읽어오기
# df=pd.read_csv('score.txt',sep=',',index_col='지원번호')
# print(df)

# # excel 파일 읽어오기
# df=pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)
# print(df.index) # 엑셀로 불러오면 index가 사라짐

