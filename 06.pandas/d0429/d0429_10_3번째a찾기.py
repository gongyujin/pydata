import pandas as pd

df=pd.read_excel('user.xlsx')
print(df)

# # first_name 컬럼 de라는 글자 있으면 출력
# print(df['first_name'].str.contains('de',case=False))

# 대소문자 구분없이 female,male 2개의 단어 해당되는 글자가 있는지 확인
gender=['female','male']
filt=df['gender'].str.lower().isin(gender)
print(df[filt])

# 1. email 컬럼에 .com 끝나는 단어를 출력하시오.
filt=df['email'].str.endswith('.com')
print(df[filt]) # filt는 무조건 True, False 형태의 series여야함

# 2. email컬럼에서 3번째 글자가 a인 것을 출력하시오.
filt=df['email'].str[2].isin(['a'])
print(df[filt])
# (df[filt]).to_csv('a1.csv')

# aba 1번째,2번째 a가 있으면 멈춤, 시작을 2부터 시작해야함
# aba 2번째 a부터 시작을 해서 해당되는 3번째 글자 a를 찾아줌
filt=df['email'].str.find('a',2)
print(df[filt==2]) # True, False를 만들어주기 위해서 filt==2 조건식을 집어넣어준다
# (df[filt==2]).to_csv('a2.csv')

