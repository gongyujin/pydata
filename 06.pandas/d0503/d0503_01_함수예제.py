import pandas as pd
from random import *

def week(num):
    if num==0:
        day='월'
    elif num==1:
        day='화'
    elif num==2:
        day='수'
    elif num==3:
        day='목'
    elif num==4:
        day='금'
    elif num==5:
        day='토'
    elif num==6:
        day='일'
    return day


df=pd.read_excel('score.xlsx',index_col='지원번호')

# 1. 요일컬럼 추가
# 2. 0-6까지 숫자를 랜덤으로 입력
# 3. 함수생성
#  0-월,1-화,2-수,... 6-일 입력
#  4. 요일 컬럼을 키 바로 뒤로 컬럼순서를 변경하시오.

df['요일']=0
# # columns 컬럼 수정
# df['요일'][0]=0
# df['요일'][1]=1

# # row index 수정
# df.loc['1번','요일']=1
# df.loc['2번','요일']=2
# # row iloc index 수정
# df.iloc[0,9]=1

# print(df.index)
# # row 개수
# print(len(df.index))
# print(df.columns)
# # column 개수
# print(len(df.columns))

# 0-6까지 숫자를 랜덥으로 입력 - 함수사용하지않고 랜덤사용
for i in range(len(df.index)):
    df['요일'][i]=randint(0,6)
# df['요일']=뒤부분을 list타입을 입력하면 됨
# df['요일']=[randint(0,6) for i in range(8)] 

df['요일']=df['요일'].apply(week)

cols=list(df.columns)
df=df[cols[0:3]+[cols[-1]]+cols[3:-1]]

print(df)