import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')

# 이름컬럼을 str변환, startswith함수적용
# 김으로 시작하는 이름
filt=df['이름'].str.startswith('김')
print(df[filt]) # not을 출력하려면 ~

print(filt) 

filt=df['이름'].str.contains('근')
print(df[filt]) # 근이 포함되어 있는 이름 검색
# print(df[~filt])  근이 포함되지 않은 이름 검색

# print(type(df['이름']))
# print(type(list(df['이름'])))
# # print((df['이름'][0]).str.replace())
# print(type(df['이름'][0]))