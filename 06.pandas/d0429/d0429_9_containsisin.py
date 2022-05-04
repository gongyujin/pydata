from operator import index
import pandas as pd

df=pd.read_excel('user.xlsx')
# de포함되어 있는 이름을 검색하시오. 대소문자 구분 없음
filt=df['first_name'].str.contains('De')|df['first_name'].str.contains('de')
print(df[filt])
# case=False 이면 대소문자 구분없음. Nan처리 : na=True, na=False, Nan
filt=df['first_name'].str.contains('de',case=False)
print(df[filt])
# print(len(df[filt])) # 49개


# isin은 list 타입이 들어올수 있음
df=pd.read_excel('score.xlsx')
print(df)

filt=df['SW특기'].str.contains('java',case=False,na=False)
print(filt)
print(df[filt]) # NaN이 있기때문에 error가 남, 대신 na=True나 False로 정의해주면 에러가 나지않음

# isin 해당되는 글자가 있는지 확인해서 출력, 완전히 일치되는 글자만 return함
langs=['python','java']
filt=df['SW특기'].str.lower().isin(langs)

print(df[filt])

# isin() : ~에 포함되어 있는지 확인
# langs=['De','de']
# filt=df['first_name'].str.lower().isin(langs)
# print(df[filt])


# # De시작하는 이름을 검색하시오.
# print(df[df['first_name'].str.startswith('De')])
